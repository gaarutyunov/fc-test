import io
from pathlib import Path

from pipe import run


def test_bonus_pipeline():
    res = io.StringIO()
    src = Path(__file__).parent

    run(src / "data/pricat.csv", src / "data/mappings_bonus.csv", res, num_processes=4)

    with open(src / "snapshots/bonus.json", "r") as f:
        expected = f.read()
    assert res.getvalue() == expected


def test_bonus_sequential_pipeline():
    res = io.StringIO()
    src = Path(__file__).parent

    run(src / "data/pricat.csv", src / "data/mappings_bonus.csv", res, num_processes=1)

    with open(src / "snapshots/bonus.json", "r") as f:
        expected = f.read()
    assert res.getvalue() == expected
