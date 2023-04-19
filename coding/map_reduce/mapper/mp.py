import multiprocessing
from typing import Generic, Iterable, TypeVar

from map_reduce.map import Map

from .base import Mapper

__all__ = ["MultiprocessingMapper"]

T = TypeVar("T")
T_r = TypeVar("T_r")


class MultiprocessingMapper(Generic[T, T_r], Mapper[T, T_r]):
    """Map inputs using multiprocessing.Pool.map()"""

    def __init__(
        self, maps: Iterable[Map[T, T_r]], num_processes: int = 1, chunk_size: int = 1
    ):
        super().__init__(maps)
        self.num_processes = num_processes
        self.chunk_size = chunk_size

    def map(self, inputs: Iterable[T]) -> Iterable[T_r]:
        with multiprocessing.Pool(self.num_processes) as pool:
            return pool.map(self._map_func, inputs, chunksize=self.chunk_size)

    def _map_func(self, item: T) -> T_r:  # pragma: no cover
        for func in self.maps:
            item = func(item)
        return item  # type: ignore
