"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730448488"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
a: str = "You will get a 4.0 GPA!"
b: str = "Oh no..."
c: str = "Pet a dog today will you?"
d: str = "You've eaten a lot of these already..."

num: int = randint(1, 4)

print("Your fortune cookie says...")

if num == 1:
    print(a)
else:
    if num == 2:
        print(b)
    else:
        if num == 3:
            print(c)
        else:
            print(d)

print("Now, go spread positive vibes!")
