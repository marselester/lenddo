"""
lenddo.exceptions
~~~~~~~~~~~~~~~~~

This module contains Lenddo exceptions.

"""


class LenddoException(Exception):
    """Base Lenddo exceptions class."""


class APIConnectionError(LenddoException):
    """Network communication errors."""


class AuthError(LenddoException):
    """Authentication and authorization errors."""
    def __init__(self, message, http_content=None, http_status_code=None):
        super(AuthError, self).__init__(message)
        self.http_content = http_content
        self.http_status_code = http_status_code


class APIError(LenddoException):
    """API server errors, for example, invalid response object."""
    def __init__(self, message, http_content, http_status_code):
        super(APIError, self).__init__(message)
        self.http_content = http_content
        self.http_status_code = http_status_code


class InvalidRequestError(LenddoException, ValueError):
    """Invalid request param errors."""
    def __init__(self, message, http_content=None, http_status_code=None):
        super(InvalidRequestError, self).__init__(message)
        self.http_content = http_content
        self.http_status_code = http_status_code
