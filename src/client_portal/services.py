from __future__ import annotations

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import QuerySet

from client_portal.exceptions import (
    InvalidCredentialsError, 
    ReservationCancellationNotAllowedError, 
    ReservationCancellationReasonRequiredError, 
    ReservationOwnershipError
)
from reservations.constants import (
    RESERVATION_STATUS_CANCELLED, 
    RESERVATION_STATUS_CONFIRMED, 
    RESERVATION_STATUS_REQUESTED
)
from reservations.models import Customer, Reservation


class ClientPortalAuthService:
    def authenticate_client(self, *, email: str, password: str) -> Customer:
        user = User.objects.filter(email=email).select_related("customer_profile").first()
        if user is None or user.is_staff or not hasattr(user, "customer_profile"):
            raise InvalidCredentialsError()

        authenticated = authenticate(username=user.username, password=password)
        if authenticated is None or not authenticated.is_active:
            raise InvalidCredentialsError()

        return authenticated.customer_profile


class ClientReservationQueryService:
    def get_customer_reservations(self, *, customer_id) -> QuerySet[Reservation]:
        return Reservation.objects.filter(customer_id=customer_id).select_related("room")


class ClientReservationLifecycleService:
    @transaction.atomic
    def cancel_reservation(
        self,
        *,
        reservation_id,
        customer,
        reason: str,
    ) -> Reservation:
        try:
            reservation = Reservation.objects.select_for_update().get(
                pk=reservation_id
            )

        except Reservation.DoesNotExist:
            raise ReservationCancellationNotAllowedError()

        if reservation.customer_id != customer.id:
            raise ReservationOwnershipError()

        if not reason or not reason.strip():
            raise ReservationCancellationReasonRequiredError()

        allowed_statuses = [
            RESERVATION_STATUS_REQUESTED,
            RESERVATION_STATUS_CONFIRMED,
        ]

        if reservation.status not in allowed_statuses:
            raise ReservationCancellationNotAllowedError()

        reservation.status = RESERVATION_STATUS_CANCELLED
        reservation.cancel_reason = reason

        reservation.save(
            update_fields=[
                "status",
                "cancel_reason",
                "updated_at",
            ]
        )

        return reservation