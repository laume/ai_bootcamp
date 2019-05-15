from hand import Hand
import itertools


def resolve_best_hand(cards) -> Hand:
    return max([Hand(cards) for cards in itertools.combinations(cards, 5)])


def determine_winner():
    pass
