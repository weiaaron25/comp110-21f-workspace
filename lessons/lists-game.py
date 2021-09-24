"""Example from LS13"""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1,6))

print(rolls)

rolls.pop()
print(rolls)

i: int = 0
sum: int = 0

while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")