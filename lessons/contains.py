"""Example of a function that processes a list."""


def main() -> None:
    names: list[str] = ['Aaron', 'Caroline']
    print(contains('Caroline', names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Function that looks for needle in haystack"""
    # We can give two arguments: a needle value we're searching for in a haystack list
    # Return true if needle is found in haystack, false otherwise
    # Loop through each index in list
    i: int = 0
    while i < len(haystack):
        # test if item stored at index is equal to needle
        if haystack[i] == needle:
            return True
        i += 1
        # Return true if so
    # Return false after testing each item
    return Falseq


if __name__ == '__main__':
    main()