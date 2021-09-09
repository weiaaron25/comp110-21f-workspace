"""Drawing forests in a loop."""

__author__ = "730448488"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 1
while i <= depth:
    print(TREE * i)
    i = i + 1