"""Custom exceptions, so the API can turn each kind of failure into a clear HTTP answer.

    ConfigurationError -> 503  (a setting is missing, e.g. no GOOGLE_API_KEY, no index ID)
    IngestionError     -> 422  (the file could not be read or indexed)
"""

class MeridianError(Exception):
    """Base class for all custom exceptions in the Meridian AI backend."""

class ConfigurationError(MeridianError):
    """Raised when a required configuration setting is missing or invalid."""

class IngestionError(MeridianError):
    """Raised when a file could not be read or indexed."""