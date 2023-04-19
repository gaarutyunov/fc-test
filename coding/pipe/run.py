import dataclasses
import json
import os
import sys
from typing import TextIO, Union

from map_reduce.io import CSVReader
from map_reduce.map import maps_from_csv

from map_reduce.mapper import Mapper, MultiprocessingMapper, SequentialMapper
from map_reduce.pipeline import Pipeline
from map_reduce.reduce import GroupByReduce
from map_reduce.reducer import Reducer

from pipe.reducer import CatalogReduce


class Encoder(json.JSONEncoder):
    """JSON encoder that can handle dataclasses."""

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(
                o,
                dict_factory=lambda x: {
                    k: v for (k, v) in x if v is not None and len(v) > 0
                },
            )
        return super().default(o)  # pragma: no cover


def run(
    data: Union[str, os.PathLike],
    mappings: Union[str, os.PathLike],
    output: TextIO = sys.stdout,
    num_processes: int = 1,
    chunk_size: int = 1,
):
    """Run the pipeline"""
    reader = CSVReader(data)
    maps = maps_from_csv(mappings)

    if num_processes <= 1:
        mapper: Mapper = SequentialMapper(maps)
    else:
        mapper = MultiprocessingMapper(maps, num_processes, chunk_size)

    reducer: Reducer = Reducer(
        [GroupByReduce("brand"), GroupByReduce("article_number"), CatalogReduce()]
    )

    pipeline = Pipeline(reader, mapper, reducer)

    res = pipeline.run()

    json.dump(res, output, indent=2, cls=Encoder, allow_nan=False, sort_keys=True)
