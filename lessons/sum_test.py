"""Testing sum.py."""

from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0


def test_sum_single_digit() -> None:
    xs: list[float] = [6.0]
    assert sum(xs) == 6.0


def test_sum_many_items() -> None: 
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0