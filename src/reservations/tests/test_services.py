import pytest
from django.contrib.auth.models import Permission

from reservations.constants import (
    RESERVATION_STATUS_CANCELLED,
    RESERVATION_STATUS_CONFIRMED,
    RESERVATION_STATUS_ON_HOLD,
)
from reservations.exceptions import (
    ReservationHoldReasonRequiredError,
    ReservationPermissionDeniedError,
    ReservationStatusTransitionError,
)
from reservations.services import ReservationLifecycleService
from reservations.tests.factories import ReservationFactory

@pytest.mark.django_db
def test_confirm_reservation_moves_requested_to_confirmed():
    reservation = ReservationFactory(status="requested")

    ReservationLifecycleService().confirm_reservation(
        reservation_id=reservation.id
    )

    reservation.refresh_from_db()

    assert reservation.status == RESERVATION_STATUS_CONFIRMED


@pytest.mark.django_db
def test_confirm_reservation_rejects_invalid_transition():
    reservation = ReservationFactory(
        status=RESERVATION_STATUS_CANCELLED
    )

    with pytest.raises(ReservationStatusTransitionError):
        ReservationLifecycleService().confirm_reservation(
            reservation_id=reservation.id
        )


@pytest.mark.django_db
def test_hold_reservation_moves_requested_to_on_hold():
    reservation = ReservationFactory(status="requested")

    actor = reservation.customer.user

    permission = Permission.objects.get(
        codename="hold_reservation"
    )

    actor.user_permissions.add(permission)

    ReservationLifecycleService().hold_reservation(
        reservation_id=reservation.id,
        hold_reason="Payment verification pending",
        actor=actor,
    )

    reservation.refresh_from_db()

    assert reservation.status == RESERVATION_STATUS_ON_HOLD
    assert reservation.hold_reason == "Payment verification pending"


@pytest.mark.django_db
def test_hold_reservation_requires_reason():
    reservation = ReservationFactory(status="requested")

    actor = reservation.customer.user

    permission = Permission.objects.get(
        codename="hold_reservation"
    )

    actor.user_permissions.add(permission)

    with pytest.raises(ReservationHoldReasonRequiredError):
        ReservationLifecycleService().hold_reservation(
            reservation_id=reservation.id,
            hold_reason="",
            actor=actor,
        )


@pytest.mark.django_db
def test_hold_reservation_requires_permission():
    reservation = ReservationFactory(status="requested")

    actor = reservation.customer.user

    with pytest.raises(ReservationPermissionDeniedError):
        ReservationLifecycleService().hold_reservation(
            reservation_id=reservation.id,
            hold_reason="Pending review",
            actor=actor,
        )


@pytest.mark.django_db
def test_hold_reservation_rejects_invalid_transition():
    reservation = ReservationFactory(
        status=RESERVATION_STATUS_CANCELLED
    )

    actor = reservation.customer.user

    permission = Permission.objects.get(
        codename="hold_reservation"
    )

    actor.user_permissions.add(permission)

    with pytest.raises(ReservationStatusTransitionError):
        ReservationLifecycleService().hold_reservation(
            reservation_id=reservation.id,
            hold_reason="Pending review",
            actor=actor,
        )