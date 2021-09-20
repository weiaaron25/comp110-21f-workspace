"""BATTLESHIP!"""
import random
import time

__author__ = "730448488"
play: bool = True


def name_func(name: str) -> str:
    """Asks user where they want to place ships; includes name."""
    return (f"{name}, where will you put your ship?")


def create_field(field: list[list[str]]) -> list[list[str]]:
    """Creates a field of water emojis to the passed field."""
    field = [[" ", "A", " B", " C", " D", " E"],
             ["1", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A"],
             ["2", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A"],
             ["3", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A"],
             ["4", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A"],
             ["5", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A", "\U0001F30A"]]
    return field


field_player: list[list[str]] = []
field_player = create_field(field_player)

field_comp: list[list[str]] = []
field_comp = create_field(field_comp)

player_view: list[list[str]] = []
player_view = create_field(player_view)

points: int = 0
player_turn: bool = True
ship_num: int = 1
player_ships_hit: int = 0
comp_ships_hit: int = 0
SHIP: str = "\U0001F6A2"
SHIP_HIT: str = "\U0001F525"
MISS: str = "\U0001F980"
ASCII_VALUE_OF_A: int = 65
win: int = 0
POINTS_FOR_WIN = 5
POINTS_FOR_LOSS = -1


print("The year is 2022. WWIII has erupted after Germany declared it a 'disgrace' that Aaron didn't get an A in COMP110. To your dismay, you've been drafted to the Navy. War is brutal. You see good men hobbling on snapped limbs and you smell flesh burning above deck. Thankfully, you have some downtime so you deicide to play some battleship with your buddies.")
player: str


def greet() -> None:
    """Greet Function."""
    global player
    player = input("What's your name? ")


def print_field(field: list[list[str]]) -> None:
    """Prints each list in the matrix."""
    for i in range(0, 6):
        print(field[i])


def place_ships(ship_num: int) -> int:
    """Asks where the user would like to place however many ships they designated to play with."""
    print("\n")
    print("Format:\nHorizontal: A-E\nVertical: 1-5\nExample: C2")
    for i in range(ship_num):
        print_field(field_player)
        bad_loc: bool = True
        while bad_loc:
            global player
            print(name_func(player))
            loc: str = input()
            if len(loc) > 2:
                print("\n")
                print("That's not a valid location")
            else:
                bad_loc = False
        x = ord(loc[0]) - ASCII_VALUE_OF_A + 1
        y = int(loc[1])
        field_player[y][x] = SHIP
    print("\n")
    print_field(field_player)
    return ship_num


def comp_place_ships(ship_num: int) -> None:
    """Randomly places ship emojis in the computer field."""
    for i in range(ship_num):
        x: int = random.randint(1, 5)
        y: int = random.randint(1, 5)
        field_comp[y][x] = SHIP


def player_attack() -> None:
    """Lets the user pick a spot on the computer board to fire at."""
    print_field(player_view)
    loc: str = input("Where will you fire? ")
    x = ord(loc[0]) - ASCII_VALUE_OF_A + 1
    y = int(loc[1])
    if field_comp[y][x] == SHIP:
        print("You hit a ship!")
        field_comp[y][x] = SHIP_HIT
        player_view[y][x] = SHIP_HIT
        global comp_ships_hit
        comp_ships_hit = comp_ships_hit + 1
    else:
        print("Miss")
        player_view[y][x] = MISS
        global player_turn
        player_turn = False


def comp_attack() -> None:
    """Computer picks a random spot on the user board to attack."""
    print("Your opponent is attacking...")
    time.sleep(2.0)
    x: int = random.randint(1, 5)
    y: int = random.randint(1, 5)
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
    """Alternates between the user and computer turn and deliminates when the game ends."""
    while player_ships_hit < ship_num and comp_ships_hit < ship_num:
        if player_turn:
            print("Your move")
            player_attack()
        if not player_turn:
            print("Opponent's move")
            comp_attack()
    if player_ships_hit == ship_num:
        global win
        win = 0
 
    else:
        win = 1


def update_points(points: int) -> int:
    """Updates points."""
    global win
    if win == 1:
        print("\n")
        print("YEAHHHH YOU WON")
        total = points + POINTS_FOR_WIN
        return total
    else:
        print("\n")
        print("You lose :(")
        total = points + POINTS_FOR_LOSS
        return total


def main() -> None:
    """Main function."""
    g = globals()
    while g['play']:
        greet()
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
        global points
        points = update_points(points)
        print(f"You have {points} points")
        r = input("Would you like to play again? (y/n) ")
        if r == "y":
            g['play'] = True
        elif r == "n":
            g['play'] = False


if __name__ == "__main__":
    main()
