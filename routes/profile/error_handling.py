class ProfileError(Exception):
    """Base class for profile-related errors."""
    pass

class ValidationError(ProfileError):
    """Raised when validation fails."""
    def __init__(self, message, field_name=None):
        super().__init__(message)
        self.field_name = field_name

class DatabaseError(ProfileError):
    """Raised when a database operation fails."""
    pass

def handle_error(error):
    """Handle errors and return appropriate messages."""
    if isinstance(error, ValidationError):
        return str(error), 'error', error.field_name
    elif isinstance(error, DatabaseError):
        return str(error), 'error', None
    else:
        return "An unexpected error occurred.", 'error', None
