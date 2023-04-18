# fc-test

[![codecov](https://codecov.io/gh/gaarutyunov/fc-test/branch/main/graph/badge.svg?token=23W0N4BUAP)](https://codecov.io/gh/gaarutyunov/fc-test)

Fashion Cloud Test Project

## Task

The [task](docs%2FFashion_Cloud_Test_Assignment_-_Python.pdf) is in the `docs` folder.

## Structure

The project is structured as follows:

- coding: Source code of the coding challenge. More info in the [README](coding%2FREADME.md)
- thinking: Flow-diagram and notes. More info in the [README](thinking%2FREADME.md)
- architecture: AWS architecture diagram and notes. More info in the [README](architecture%2FREADME.md)

## Prerequisites

1. [Python 3.9](https://www.python.org/downloads/)
2. [Poetry](https://python-poetry.org/docs/#installation)

> **Note** Poetry is used for virtual environment management.
It is not required to run the code, but it is recommended for development.

## Steps to test the code

1. Install the dependencies with (If you are using poetry)

```shell
cd coding && poetry install
```

2. Put data into the `coding/tests/data` folder
3. Run tests with (If you are using poetry)

```shell
cd coding && poe test
```

4. Or with:

```shell
cd coding && pytest
```
