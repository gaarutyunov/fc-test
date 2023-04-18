from pathlib import Path

import perftester

from pipe import run


def test_benchmark_basic():
    src = Path(__file__).parent

    perftester.time_test(run, data=src / "data/pricat.csv", mappings=src / "data/mappings.csv", num_processes=1, Number=1000, Repeat=5, raw_limit=25e-05)
    perftester.time_test(run, data=src / "data/pricat.csv", mappings=src / "data/mappings.csv", num_processes=8, Number=1000, Repeat=5, raw_limit=25e-05)


def test_benchmark_bonus():
    src = Path(__file__).parent

    perftester.time_test(run, data=src / "data/pricat.csv", mappings=src / "data/mappings_bonus.csv", num_processes=1, Number=1000, Repeat=5, raw_limit=25e-05)
    perftester.time_test(run, data=src / "data/pricat.csv", mappings=src / "data/mappings_bonus.csv", num_processes=8, Number=1000, Repeat=5, raw_limit=25e-05)
