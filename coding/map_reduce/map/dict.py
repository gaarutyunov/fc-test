from typing import Dict, Generic, TypeVar

from .base import Map


K = TypeVar("K")
V = TypeVar("V")


class ColumnMap(Generic[K, V], Map[Dict[K, V], Dict[K, V]]):
    """Map a value in a dictionary to a new key with updated value."""

    def __init__(
        self, source: K, destination: K, source_value: V, destination_value: V
    ) -> None:
        self.source = source
        self.destination = destination
        self.source_value = source_value
        self.destination_value = destination_value

    def check(self, inp: Dict[K, V]) -> bool:
        return self.key(inp) == self.source_value

    def map(self, inp: Dict[K, V]) -> Dict[K, V]:
        return {**inp, self.destination: self.destination_value}

    def key(self, inp: Dict[K, V]) -> V:
        """Get key to compare the source value to."""
        return inp[self.source]


class MultiColumnMap(Generic[V], ColumnMap[str, V]):
    """Map a value in a dictionary to a new key with updated value.
    The source key is a string with multiple keys separated by a delimiter."""

    def __init__(
        self,
        source: str,
        destination: str,
        source_value: V,
        destination_value: V,
        delimiter: str,
    ) -> None:
        super().__init__(source, destination, source_value, destination_value)
        self.delimiter = delimiter
        self.split_source = self.source.split(self.delimiter)

    def key(self, inp: Dict[str, V]) -> V:
        return self.delimiter.join(inp[key] for key in self.split_source)  # type: ignore


class ConcatMap(MultiColumnMap[str]):
    """Concatenate multiple values in a dictionary to a new key with `destination_value` as a delimiter."""

    def __init__(
        self,
        source: str,
        destination: str,
        source_value: str,
        destination_value: str,
        delimiter: str,
    ) -> None:
        super().__init__(
            source, destination, source_value, destination_value, delimiter
        )

    def check(self, inp: Dict[str, str]) -> bool:
        return True

    def map(self, inp: Dict[str, str]) -> Dict[str, str]:
        return {
            **inp,
            self.destination: self.destination_value.join(
                inp[key] for key in self.split_source
            ),
        }
