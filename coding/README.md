# Coding challenge

The solution is based on the MapReduce paradigm.

In production we would use a distributed framework like Hadoop or Spark.

## Structure

The project is structured as follows:
- map_reduce: simple framework for data processing
- pipe: task specific pipeline implementations

## Usage

1. To run basic pipeline run:

```shell
python -m pipe --data tests/data/pricat.csv \
                   --mappings tests/data/mappings.csv \
                   --output basic_output.json \
                   --num_processes 4
```

2. To run bonus pipeline run:

```shell
python -m pipe --data tests/data/pricat.csv \
                   --mappings tests/data/mappings_bonus.csv \
                   --output bonus_output.json \
                   --num_processes 4
```