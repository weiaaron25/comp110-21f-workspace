"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730448488"


def test_only_evens() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens2() -> None:
    ys: list[int] = [12903120947123094, 9283784392039841290, 9128312804739487]
    assert only_evens(ys) == [12903120947123094, 9283784392039841290]


def test_only_evens3() -> None:
    zs: list[int] = [0, 0, 0, -999]
    assert only_evens(zs) == [0, 0, 0]


def test_sub() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(xs, 0, 3) == [1, 2]


def test_sub2() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(xs, 4, 5) == [4]


def test_sub3() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(xs, -999, 999) == [1, 2, 3, 4, 5]


def test_concat1() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert concat(xs, xs) == xs + xs


def test_concat2() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    ys: list[int] = [77, 23]
    assert concat(xs, ys) == xs + ys


def test_concat3() -> None:
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == xs + ys