from __future__ import annotations


class AppError(Exception):
    code = "application_error"
    detail = "Application error."
    family = "domain"
    errors: list[dict] | None = None

    def __init__(
        self,
        detail: str | None = None,
        *,
        code: str | None = None,
        errors: list[dict] | None = None,
    ) -> None:
        self.detail = detail or self.detail
        self.code = code or self.code
        self.errors = errors
        super().__init__(self.detail)


class AuthError(AppError):
    family = "auth"


class DomainError(AppError):
    family = "domain"
