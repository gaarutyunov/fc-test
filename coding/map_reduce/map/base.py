import abc
from typing import Generic, TypeVar

__all__ = ["Map"]

T = TypeVar("T")
T_r = TypeVar("T_r")


class Map(abc.ABC, Generic[T, T_r]):
    @abc.abstractmethod
    def map(self, inp: T) -> T_r:
        """Map an input to an output."""

    @abc.abstractmethod
    def check(self, inp: T) -> bool:
        """Check if the input should be mapped."""

    def __call__(self, inp: T) -> T_r:
        if not self.check(inp):
            return inp
        return self.map(inp)
