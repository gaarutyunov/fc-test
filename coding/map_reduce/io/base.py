import abc
from typing import Generic, Iterable, TypeVar

__all__ = ["Reader"]

T_r = TypeVar("T_r")


class Reader(abc.ABC, Generic[T_r]):
    @abc.abstractmethod
    def read(self) -> Iterable[T_r]:
        """Read data from a source and return an iterable of data."""
