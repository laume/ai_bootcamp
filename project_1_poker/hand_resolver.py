from hand import Hand
import itertools


def resolve_best_hand(cards) -> Hand:
    hands = [Hand(cards) for cards in itertools.combinations(cards, 5)]

    for hand in sorted(hands):
        print(f"{hand} score is {hand.score}")

    return max(hands)


def determine_winner():
    pass
