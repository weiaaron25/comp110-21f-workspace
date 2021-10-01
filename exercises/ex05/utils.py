"""List utility functions part 2."""

__author__ = "730448488"

# Define your functions below


def only_evens(nums: list[int]) -> list[int]:
    """Function that returns only the evens in a list of ints."""
    evens: list[int] = []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
    return evens


def sub(nums: list[int], start: int, finish: int) -> list[int]:
    """Function that gives a range in a list of ints."""
    if start <= 0:
        start = 1
    if finish > len(nums):
        finish = len(nums)
    new_list: list[int] = []
    new_list = nums[start - 1:finish - 1]
    return new_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Function that combines two lists of ints."""
    new_list: list[int] = []
    new_list = list1 + list2
    return new_list