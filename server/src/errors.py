"""Errors"""


class UniqueEmailError(Exception):
    """Exception raised when a user tries to register with an email that already exists."""

    def __init__(self, message: str = "Email already exists.") -> None:
        self.message: str = message
        super().__init__(self.message)
