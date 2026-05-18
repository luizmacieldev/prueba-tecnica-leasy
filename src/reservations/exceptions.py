from shared.errors import DomainError


class ReservationError(DomainError):
    code = "reservation_error"
    detail = "Reservation error."


class ReservationNotFoundError(ReservationError):
    code = "reservation_not_found"
    detail = "Reservation not found."


class ReservationStatusTransitionError(ReservationError):
    code = "reservation_invalid_transition"
    detail = "Reservation cannot transition from its current status."

class ReservationHoldReasonRequiredError(ReservationError):
    code = "reservation_hold_reason_required"
    detail = "Hold reason is required."


class ReservationPermissionDeniedError(ReservationError):
    code = "reservation_permission_denied"
    detail = "You do not have permission to hold reservations."