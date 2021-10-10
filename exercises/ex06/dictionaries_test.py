"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert() -> None: 
    """Tests function."""
    xs: dict = {'apple': 'apple', 'pear': 'Orange'}
    assert invert(xs) == {'apple': 'apple', 'Orange': 'pear'}


def test_invert2() -> None: 
    """Tests function."""
    xs: dict = {'apple': 'apple', 'pear': 'Orange', 'Pineapple': 'plum'}
    assert invert(xs) == {'apple': 'apple', 'Orange': 'pear', 'plum': 'Pineapple'}


def test_invert3() -> None: 
    """Tests function."""
    xs: dict = {'apple': 'apple', 'pear': 'Orange', 'Pineapple': 'plum'}
    assert invert(xs) == {'apple': 'apple', 'Orange': 'pear', 'plum': 'Pineapple'}


def test_favorite_color() -> None:
    """Tests function."""
    xs: dict = {'Adam': 'Yellow', 'Tom': 'Blue', 'Marc': 'Yellow'}
    assert favorite_color(xs) == "Yellow"


def test_favorite_color2() -> None:
    """Tests function."""
    xs: dict = {'John': 'Pink', 'Milo': 'Green', 'Greg': 'Green'}
    assert favorite_color(xs) == "Green"


def test_favorite_color3() -> None:
    """Tests function."""
    xs: dict = {'Gracie': 'Sapphire', 'Matild': 'Red', 'Harper': 'Red', 'Elton': 'Sapphire'}
    assert favorite_color(xs) == "Sapphire"


def test_count() -> None:
    """Tests function."""
    xs: list = ["grapes", "mango", "watermelon", "mango"]
    assert count(xs) == {"grapes": 1, "mango": 2, "watermelon": 1}


def test_count2() -> None:
    """Tests function."""
    xs: list = ["knives", "forks", "knives", "knives"]
    assert count(xs) == {"knives": 3, "forks": 1}


def test_count3() -> None:
    """Tests function."""
    xs: list = ["grapes", "mango", "watermelon", "mango"]
    assert count(xs) == {"grapes": 1, "mango": 2, "watermelon": 1}