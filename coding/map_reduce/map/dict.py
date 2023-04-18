from typing import Dict

from .base import Map


class ColumnMap(Map[Dict[str, str], Dict[str, str]]):
    def __init__(
        self, source: str, destination: str, source_value: str, destination_value: str
    ) -> None:
        self.source = source
        self.destination = destination
        self.source_value = source_value
        self.destination_value = destination_value

    def check(self, inp: Dict[str, str]) -> bool:
        return self.key(inp) == self.source_value

    def map(self, inp: Dict[str, str]) -> Dict[str, str]:
        return {**inp, self.destination: self.destination_value}

    def key(self, inp: Dict[str, str]) -> str:
        return inp[self.source]


class MultiColumnMap(ColumnMap):
    def __init__(
        self,
        source: str,
        destination: str,
        source_value: str,
        destination_value: str,
        delimiter: str,
    ) -> None:
        super().__init__(source, destination, source_value, destination_value)
        self.delimiter = delimiter
        self.split_source = self.source.split(self.delimiter)

    def key(self, inp: Dict[str, str]) -> str:
        return self.delimiter.join(inp[key] for key in self.split_source)


class ConcatMap(MultiColumnMap):
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
