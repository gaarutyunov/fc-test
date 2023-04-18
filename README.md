# fc-test

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

## Steps to run the code

1. Install the dependencies with

```shell
cd coding && poetry install
```

2. Put data into the `coding/tests/data` folder
3. Run tests with

```shell
cd coding && poe test
```