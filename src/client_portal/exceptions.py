from shared.errors import AuthError


class InvalidCredentialsError(AuthError):
    code = "auth_invalid_credentials"
    detail = "Invalid email or password."


class InvalidTokenError(AuthError):
    code = "auth_invalid_token"
    detail = "Invalid access token."
