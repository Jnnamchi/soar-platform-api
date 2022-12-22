class RepositoryError(Exception):
    """Base repository error"""


class DoesNotExists(RepositoryError):
    """Object not found in database"""


class AlreadyExists(RepositoryError):
    """Object already exists"""

