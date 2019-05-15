from player import Player
from table import Table
import os
import time

playing = True

p1 = Player("Martynas", 1000)
table = Table(p1)


def after_flop() -> bool:
    action = input("Do you want to (b)et or (f)old?: ")

    if action.lower() == 'f':
        return False
    if action.lower() == 'b':
        return True
    else:
        print(f"Invalid action: {action}. Only 'f' (for Fold) or 'b' (for Bet) are allowed")
        return after_flop()


def want_to_play_again() -> bool:
    play_again = input("Play again? (y/n): ")

    if play_again == 'n':
        return False
    else:
        return True


def clear_screen():
    os.system('clear')


while playing:
    table.new_game()

    print(table)

    bet = after_flop()
    if bet:
        print(f"{p1.name} bets.")
        table.player_bets()
        table.resolve_winner()
        time.sleep(3)
    else:
        table.player_folds()
        print(f"{p1.name} folds.")
        time.sleep(1)

    if not want_to_play_again():
        playing = False
    else:
        clear_screen()

clear_screen()
print("Thank you for playing!")