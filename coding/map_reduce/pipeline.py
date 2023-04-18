from typing import Generic, TypeVar

from map_reduce.io import Reader
from map_reduce.mapper import Mapper
from map_reduce.reducer import Reducer

T = TypeVar("T")
T_r = TypeVar("T_r")
T_o = TypeVar("T_o")

__all__ = ["Pipeline"]


class Pipeline(Generic[T, T_r, T_o]):
    def __init__(
        self, inputs: Reader, mapper: Mapper[T, T_r], reducer: Reducer[T_r, T_o]
    ):
        self.inputs = inputs
        self.mapper = mapper
        self.reducer = reducer

    def run(self) -> T_o:
        mapped = self.mapper(self.inputs)
        return self.reducer(mapped)
