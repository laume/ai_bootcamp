from hand import Hand
from typing import List
from card import Card
import itertools


def resolve_best_hand(cards: List[Card]) -> Hand:
    hands = [Hand(cards) for cards in itertools.combinations(cards, 5)]

    # for hand in sorted(hands):
    #     print(f"{hand} score is {hand.score}")

    return max(hands)

