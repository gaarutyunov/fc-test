from typing import Generic, Iterable, TypeVar

from map_reduce.mapper import Mapper

__all__ = ["SequentialMapper"]

T = TypeVar("T")
T_r = TypeVar("T_r")


class SequentialMapper(Generic[T, T_r], Mapper[T, T_r]):
    """Map inputs sequentially using map()"""

    def map(self, inputs: Iterable[T]) -> Iterable[T_r]:
        return map(self._map_func, inputs)

    def _map_func(self, item: T) -> T_r:
        for func in self.maps:
            item = func(item)
        return item  # type: ignore
