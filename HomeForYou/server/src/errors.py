"""Errors"""

from fastapi import HTTPException


class AppException(HTTPException):
    """An default app exception"""

    def __init__(self, status_code: int, message: str):
        super().__init__(status_code=status_code, detail=message)


class BadError(AppException):
    """Exception raised for a 400 code."""

    def __init__(self, message: str = "Bad request"):
        super().__init__(400, message)


class UnauthorizedError(AppException):
    """Exception raised for a 401 code."""

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(401, message)


class ForbiddenError(AppException):
    """Exception raised for 403 code."""

    def __init__(self, message: str = "Forbidden"):
        super().__init__(403, message)


class UniqueEmailError(Exception):
    """Exception raised when a user tries to register with an email that already exists."""

    def __init__(self, message: str = "Email already exists.") -> None:
        self.message: str = message
        super().__init__(self.message)
