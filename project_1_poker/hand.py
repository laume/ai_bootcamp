from typing import Tuple

from card import Card


class Hand:
    def __init__(self, cards: Tuple[Card, Card, Card, Card, Card]) -> None:
        self.cards = sorted(list(cards))
        self.rank: int = 0
        self.name: str = ''
        self.score: int = 0

        self._score_combination()
        self.score = self.rank

        for card in cards:
            self.score += card.value

    def _score_combination(self) -> None:
        if self.is_royal_flush():
            self.rank = 1000
            self.name = "Royal Flush"
        elif self.is_straight_flush():
            self.rank = 900
            self.name = "Straight flush"
        elif self.is_4_of_a_kind():
            self.rank = 800
            self.name = "Four of a kind"
        elif self.is_full_house():
            self.rank = 700
            self.name = "Full house"
        elif self.is_flush():
            self.rank = 600
            self.name = "Flush"
        elif self.is_straight():
            self.rank = 500
            self.name = "Straight"
        elif self.is_3_of_a_kind():
            self.rank = 400
            self.name = "Three of a kind"
        elif self.is_pair():
            self.rank = 300
            self.name = "A Pair"
        else:
            self.rank = 0
            self.name = "High card"

    def is_pair(self) -> bool:
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 2 for value, count in counts.items())

    def is_two_pair(self) -> bool:
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return 2 == len(list(filter(lambda v: v, [count == 2 for value, count in counts.items()])))

    def is_3_of_a_kind(self) -> bool:
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 3 for value, count in counts.items())

    def is_straight(self) -> bool:
        return all(x.value == y.value - 1 for x, y in zip(self.cards, self.cards[1:]))

    def is_flush(self) -> bool:
        return len(set(map(lambda card: card.suit, self.cards))) == 1

    def is_full_house(self) -> bool:
        return self.is_pair() and self.is_3_of_a_kind()

    def is_4_of_a_kind(self) -> bool:
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 4 for value, count in counts.items())

    def is_straight_flush(self) -> bool:
        return self.is_flush() and self.is_straight()

    def is_royal_flush(self) -> bool:
        return self.cards[0].value == 10 and self.is_straight() and self.is_flush()

    def __repr__(self):
        return " ".join(str(card) for card in self.cards)

    def __lt__(self, other):
        return self.score < other.score
