from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Dict, Generic, Iterable, List, TypeVar

from .base import Reduce

__all__ = ["GroupByReduce", "Grouping"]


T = TypeVar("T")


@dataclass
class Grouping(Generic[T]):
    """A grouping of values by a key."""

    key: str
    values: Iterable[Any]


class GroupByReduce(Reduce[Any, Iterable[Grouping[Any]]]):
    """Groups values by a key."""

    def __init__(self, key: str) -> None:
        self.key = key

    def reduce(self, inputs: Iterable[Any]) -> Iterable[Grouping[Any]]:
        res: Dict[str, List[Any]] = defaultdict(list)

        for inp in inputs:
            if isinstance(inp, Grouping):
                res[inp.key].extend(self.reduce(inp.values))
            else:
                res[inp[self.key]].append(inp)

        return (Grouping(key, values) for key, values in res.items())
