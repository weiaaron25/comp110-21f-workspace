"""Counting letters in a string."""

__author__ = "730448488"


# Begin your solution here...
letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")

length: int = len(word) - 1

count: int = 0

while length >= 0:
    if word[length] == letter:
        count = count + 1
        length = length - 1

    else:
        length = length - 1

finalcount: str = str(count)
print("Count: " + finalcount)
