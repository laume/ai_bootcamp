from player import Player
from table import Table
import os
import time


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
    play_again = input("Play again? (Y/n): ")

    if play_again == 'n':
        return False
    else:
        return True


def buy_in_amount() -> int:
    """
    Get buy in amount from user
    :return: preferred buy-in amount
    """
    raw_input = input("What is the amount you would like to play with? (100 minimum): ")

    try:
        amount = int(raw_input)
        if amount < 100:
            print("Minimum amount is 100!")
            return buy_in_amount()

        return amount
    except ValueError:
        print(f"{raw_input} is not a valid input! Try again.")
        return buy_in_amount()


def clear_screen():
    os.system('clear')


def start_game():
    name = input("What is your name? ")
    buy_in = buy_in_amount()

    clear_screen()

    p1 = Player(name, buy_in)
    table = Table(p1)

    playing = True
    while playing:
        table.new_game()

        print(table)

        if not table.dealer_qualifies():
            time.sleep(2)
            clear_screen()
            continue

        flop_action = after_flop()
        if flop_action:
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


if __name__ == '__main__':
    start_game()
