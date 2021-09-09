"""Finding duplicate letters in a word."""

__author__ = "730448488"

word: str = input("Enter a word: ")

letter_list = [] 
duplicate: str = "Found duplicate: False"
for letter in word:
    if letter not in letter_list:
        letter_list.append(letter)
    else:
        duplicate = "Found duplicate: True"
print(duplicate)