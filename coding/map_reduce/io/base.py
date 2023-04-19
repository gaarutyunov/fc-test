import abc


class Reader(abc.ABC):
    """Base class for all data readers."""

    @abc.abstractmethod
    def read(self):
        """Read data from a source and return an iterable of data."""
