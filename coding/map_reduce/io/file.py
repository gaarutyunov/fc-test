import os
import pathlib
from typing import Iterable, Union

from .base import Reader


class FileReader(Reader):
    """Reads a file line by line."""

    def __init__(self, path: Union[str, os.PathLike]):
        super().__init__()
        self.path = pathlib.Path(path).expanduser()

    def read(self) -> Iterable:
        with open(self.path, "r") as f:
            for line in f.readlines():
                yield line.strip()
