"""Repeating a beat in a loop."""

__author__ = "730448488"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))

beat = beat + " "

beat2: str = ""

if repeat <= 0:
    print("No beat...")

else:
    while repeat > 0:
        beat2 = beat2 + beat
        repeat = repeat - 1
    finalbeat = beat2.rstrip()
    print(finalbeat)
