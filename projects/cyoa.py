"""BATTLESHIP"""
__author__ = "730448488"
play: bool = True
import numpy
import random
import time
def name_func(name: str) -> str:
    return (f"{name}, where will you put your ship?")

def create_field(field):
    field = [[ "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A", "\U0001F30A"],
[ "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A"],
[ "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A"],
[ "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A"],
[ "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A",  "\U0001F30A"]]
    return field

field_player = []
field_player = create_field(field_player)

field_comp = []
field_comp = create_field(field_comp)

player_view = []
player_view = create_field(player_view)

points: float = 0.0
player_turn: bool = True
ship_num: int = 1
player_ships_hit: int = 0
comp_ships_hit: int = 0
SHIP: str = "\U0001F6A2"
SHIP_HIT: str = "\U0001F525"
MISS: str = "\U0001F980"
ASCII_VALUE_OF_A: int = 65

print("The year is 2022. WWIII has erupted after Germany declared it a 'disgrace' that Aaron didn't get an A in COMP110. To your dismay, you've been drafted to the Navy. War is brutal. You see good men hobbling on snapped limbs and you smell flesh burning above deck. Thankfully, you have some downtime so you deicide to play some battleship with your buddies.")
name: str = input("What's your name? ")

def print_field(field) -> None:
    for i in range(0,5):
        print(field[i])

def place_ships(ship_num: int) -> int:
    print("\n")
    print("Format:\nHorizontal: A-E\nVertical: 1-5\nExample: C2")
    for i in range(ship_num):
        print_field(field_player)
        bad_loc: bool = True
        while bad_loc == True:
            print(name_func(name))
            loc: str = input()
            if len(loc) > 2:
                print("\n")
                print("That's not a valid location")
            else:
                bad_loc = False
        x = ord(loc[0]) - ASCII_VALUE_OF_A
        y = int(loc[1]) - 1
        field_player[y][x] = SHIP
    print("\n")
    print_field(field_player)
    return ship_num

def comp_place_ships(ship_num: int):
    for i in range(ship_num):
        x: int = random.randint(0,4)
        y: int = random.randint(0,4)
        field_comp[y][x] = SHIP

def player_attack() -> None:
    print_field(player_view)
    loc: str = input("Where will you fire? ")
    x = ord(loc[0]) - ASCII_VALUE_OF_A
    y = int(loc[1]) - 1
    if field_comp[y][x] == SHIP:
        print("You hit a ship!")
        field_comp[y][x] = SHIP_HIT
        player_view[y][x] = SHIP_HIT
        global comp_ships_hit
        comp_ships_hit = comp_ships_hit + 1
        g = globals()
        g['points'] = update_points(g['points'],1)
    else:
        print("Miss")
        player_view[y][x] = MISS
        global player_turn
        player_turn = False

def comp_attack() -> None:
    print("Your opponent is attacking...")
    time.sleep(3.0)
    x: int = random.randint(0,4)
    y: int = random.randint(0,4)
    if field_player[y][x] == SHIP:
        print("One of your ships was hit!")
        field_player[y][x] = SHIP_HIT
        global player_ships_hit
        player_ships_hit = player_ships_hit + 1
    else:
        print("He missed. What a dummy.")
        global player_turn
        player_turn = True

def take_turns(ship_num: int) -> None:
    while player_ships_hit < ship_num and comp_ships_hit < ship_num:
        if player_turn:
            print("Your move")
            player_attack()
        if not player_turn:
            print("Opponent's move")
            comp_attack()
    if player_ships_hit == ship_num:
        print("\n")
        print("You lose :(")
        g = globals()
        g['points'] = update_points(g['points'],-3)
    else:
        print("\n")
        print("YEAHHHH YOU WON")
        g = globals()
        g['points'] = update_points(g['points'],5)

def update_points(points: int, new: int) -> int:
    total = points + new
    return total

def main():
    g = globals()
    while g['play']:
        g['field_player'] = create_field(g['field_player'])
        g['field_comp'] = create_field(g['field_comp'])
        g['player_view'] = create_field(g['player_view'])
        g['player_turn'] = True
        g['player_ships_hit'] = 0
        g['comp_ships_hit'] = 0
        g['ship_num'] = int(input("How many ships will you play with? "))
        print(f"Everyone has placed {place_ships(g['ship_num'])} ships")
        comp_place_ships(g['ship_num'])
        take_turns(g['ship_num'])
        print(f"You have {points} points")
        r = input("Would you like to play again? (y/n) ")
        if r == "y":
            g['play'] = True
        elif r == "n":
            g['play'] = False

if __name__ == "__main__":
    main()
