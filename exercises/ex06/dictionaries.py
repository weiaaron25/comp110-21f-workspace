"""Practice with dictionaries."""

__author__ = "123456789"

# Define your functions below


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Function that inverts a dictionary."""
    new_dict: dict[str, str] = {}
    for key, value in xs.items():
        if value in new_dict.keys():
            raise KeyError("")
        new_dict[value] = key
    return new_dict


def favorite_color(xs: dict[str, str]) -> str:
    """Function that returns favorite color."""
    new_dict: dict[str, int] = {}
    for value in xs.values():
        if value not in new_dict.keys():
            new_dict[value] = 1
        else:
            new_dict[value] += 1
    highest: int = max(new_dict.values())
    for key, value in new_dict.items():
        if value == highest:
            return key
    return "Nothing"


def count(xs: list[str]) -> dict[str, int]:
    """Counts unique items in a list."""
    d: dict[str, int] = {}
    for i in xs:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    return d