"""List utility functions."""

__author__ = "730448488"


# TODO: Implement your functions here.

# Define the all function.
def all(nums: list[int], x: int) -> bool:
    """Function that determines if all of the ints in a list are the same as a given int."""
    if len(nums) == 0:
        return False
    # create iterator.
    i: int = 0
    # iterate.
    while i < len(nums):
        if nums[i] == x:
            i += 1
        else:
            return False
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Function that determines if two lists are the same."""
    if len(x) != len(y):
        return False
    i: int = 0
    while i < len(x):
        if x[i] == y[i]:
            i += 1
        else:
            return False
    return True


def max(nums: list[int]) -> int:
    """Function that determines the max value in a list of ints."""
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    x = nums[0]
    while i < len(nums):
        if x < nums[i]:
            x = nums[i]
            i += 1
        else:
            i += 1
    return x