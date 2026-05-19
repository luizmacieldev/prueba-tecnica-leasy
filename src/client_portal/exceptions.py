from shared.errors import AuthError, AppError


class InvalidCredentialsError(AuthError):
    code = "auth_invalid_credentials"
    detail = "Invalid email or password."


class InvalidTokenError(AuthError):
    code = "auth_invalid_token"
    detail = "Invalid access token."


class ReservationCancellationNotAllowedError(AppError):
    code = "reservation_cancellation_not_allowed"
    detail = "Reservation cannot be cancelled."


class ReservationCancellationReasonRequiredError(AppError):
    code = "reservation_cancellation_reason_required"
    detail = "Cancellation reason is required."


class ReservationOwnershipError(AppError):
    code = "reservation_forbidden"
    detail = "You cannot cancel this reservation."