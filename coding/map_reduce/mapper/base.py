import abc
from typing import Any, Generic, Iterable, TypeVar

from map_reduce.io import Reader
from map_reduce.map import Map


__all__ = ["Mapper"]

T = TypeVar("T")
T_r = TypeVar("T_r")


class Mapper(abc.ABC, Generic[T, T_r]):
    """Base class for all mappers."""

    def __init__(self, maps: Iterable[Map[Any, Any]]):
        self.maps = maps

    @abc.abstractmethod
    def map(self, inputs: Iterable[T]) -> Iterable[T_r]:
        """Map an iterable of inputs to an iterable of outputs using configured maps."""

    def __call__(self, inputs: Reader) -> Iterable[T_r]:
        return self.map(inputs.read())
