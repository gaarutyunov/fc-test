# Coding challenge

* The solution is based on the MapReduce paradigm.

* In production we would use a distributed framework like Hadoop or Spark.

* The bonus mapping can be described in the mappings.csv file as follows (See last line in [mappings_bonus.csv](tests/data/mappings_bonus.csv)):

| source | destination                     | source_type             | destination_type |
|--------|---------------------------------|-------------------------|-----------------|
| *      | a space here to " ".join(values) | price_buy_net\|currency |price_buy_net_currency             |


## Structure

The project is structured as follows:
- map_reduce: simple framework for data processing
- pipe: task specific pipeline implementations


## Prerequisites

1. [Python ^3.9](https://www.python.org/downloads/)
2. [Poetry](https://python-poetry.org/docs/#installation)

> **Note**
> 
> Poetry is used for virtual environment management.
It is not required to run the code, but it is recommended for development.

## Dependencies

1. Install the dependencies (If you are using poetry):

```shell
poetry install
```

## Running tests

1. Put data into the `tests/data` folder (in case you have any additional test data)
2. Run tests (If you are using poetry):

```shell
 poe test
```

3. Or (If you have `pytest` installed):

```shell
pytest
```

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