import os
from typing import Iterable, List, Union

from map_reduce.io import CSVReader
from .dict import ColumnMap, ConcatMap, Map, MultiColumnMap


def maps_from_csv(
    path: Union[str, os.PathLike], delimiter: str = ";", multi_delimiter: str = "|"
) -> Iterable[Map]:
    reader = CSVReader(path, delimiter=delimiter)

    maps: List[Map] = []

    for line in reader.read():
        if "*" in line["source"]:
            maps.append(
                ConcatMap(
                    line["source_type"],
                    line["destination_type"],
                    line["source"],
                    line["destination"],
                    multi_delimiter,
                )
            )
        elif "|" in line["source"]:
            maps.append(
                MultiColumnMap(
                    line["source_type"],
                    line["destination_type"],
                    line["source"],
                    line["destination"],
                    multi_delimiter,
                )
            )
        else:
            maps.append(
                ColumnMap(
                    line["source_type"],
                    line["destination_type"],
                    line["source"],
                    line["destination"],
                )
            )

    return maps
