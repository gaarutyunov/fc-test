from typing import Generic, Iterable, TypeVar

from map_reduce.reduce import Reduce

__all__ = ["Reducer"]

T = TypeVar("T")
T_r = TypeVar("T_r")


class Reducer(Generic[T, T_r]):
    def __init__(self, reduces: Iterable[Reduce]) -> None:
        self.reduces = reduces

    def reduce(self, inputs: Iterable[T]) -> T_r:
        """Reduce an iterable of inputs to a single output using configured reduces."""
        for reduce in self.reduces:
            inputs = reduce(inputs)

        return inputs

    def __call__(self, inputs: Iterable[T]) -> T_r:
        return self.reduce(inputs)
