import abc
from typing import Generic, Iterable, TypeVar

__all__ = ["Reduce"]

T = TypeVar("T")
T_r = TypeVar("T_r")


class Reduce(abc.ABC, Generic[T, T_r]):
    """Base class for all reduce operations."""

    @abc.abstractmethod
    def reduce(self, inputs: Iterable[T]) -> T_r:
        """Reduce an iterable of inputs to a single output."""

    def __call__(self, inputs: Iterable[T]) -> T_r:
        return self.reduce(inputs)
