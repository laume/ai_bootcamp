from hand import Hand
from typing import List
from card import Card
import itertools


def resolve_best_hand(cards: List[Card]) -> Hand:
    hands = [Hand(cards) for cards in itertools.combinations(cards, 5)]

    # for hand in sorted(hands):
    #     print(f"{hand} score is {hand.score}")

    return max(hands)


def is_pair_of_4_or_better(cards: List[Card]) -> bool:
    hand = Hand(tuple(cards))

    if hand.rank >= 3000:
        return True  # better than pair

    if hand.is_pair():
        ranks = list(map(lambda card: card.rank, hand.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        pair_rank = list([value for value, count in counts.items() if count == 2])[0]
        return Card.values[pair_rank] >= 4

    return False
