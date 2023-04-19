import os
from typing import Dict, Iterable, Union

from .file import FileReader


class CSVReader(FileReader):
    """Reads a CSV file line by line and returns a dictionary for each line with the keys being the header values."""

    def __init__(self, path: Union[str, os.PathLike], delimiter: str = ";"):
        super().__init__(path)
        self.delimiter = delimiter

    def read(self) -> Iterable[Dict[str, str]]:
        iterator = iter(super().read())
        header = next(iterator)
        mapping = {index: key for index, key in enumerate(header.split(self.delimiter))}

        for line in iterator:
            yield {
                mapping[index]: value
                for index, value in enumerate(line.split(self.delimiter))
            }
