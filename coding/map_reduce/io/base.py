import abc


class Reader(abc.ABC):
    @abc.abstractmethod
    def read(self):
        """Read data from a source and return an iterable of data."""
