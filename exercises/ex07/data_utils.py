"""Utility functions."""

from csv import DictReader

__author__ = "730448488"

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Imports a csv."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read data file as a csv rather than strings
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all the values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Head function."""
    if rows >= len(data):
        return data
    result: dict[str, list[str]] = {}
    for column in data.keys():
        values: list[str] = []
        for i in range(rows):
            values.append(data[column][i])
        result[column] = values
    return result


def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Select function."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = data[column]
    return result


def concat(data1: dict[str, list[str]], data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat function."""
    result: dict[str, list[str]] = data1
    for column in data2.keys():
        if column in result.keys():
            for item in data2[column]:
                result[column].append(item)
        else:
            result[column] = data2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts things in list."""
    result: dict[str, int] = {}
    for item in values:
        if item not in result.keys():
            result[item] = 1
        else:
            result[item] += 1
    return result