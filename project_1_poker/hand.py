class Hand:
    def __init__(self, cards):
        self.cards = sorted(list(cards))
        self.rank = 0
        self.name = ''

        self._combination()

    def _combination(self) -> None:
        if self._is_royal_flush():
            self.rank = 1000
            self.name = "Royal Flush"
        elif self._is_straight_flush():
            self.rank = 900
            self.name = "Straight flush"
        elif self._is_4_of_a_kind():
            self.rank = 800
            self.name = "Four of a kind"
        elif self._is_full_house():
            self.rank = 700
            self.name = "Full house"
        elif self._is_flush():
            self.rank = 600
            self.name = "Flush"
        elif self._is_straight():
            self.rank = 500
            self.name = "Straight"
        elif self._is_3_of_a_kind():
            self.rank = 400
            self.name = "Three of a kind"
        elif self._is_pair():
            self.rank = 300
            self.name = "A Pair"
        else:
            self.rank = 0
            self.name = "High card"

    def _is_pair(self):
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 2 for value, count in counts.items())

    def _is_3_of_a_kind(self):
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 3 for value, count in counts.items())

    def _is_straight(self):
        return all(x.value == y.value - 1 for x, y in zip(self.cards, self.cards[1:]))

    def _is_flush(self):
        return len(set(map(lambda card: card.suit, self.cards))) == 1

    def _is_full_house(self):
        return self._is_pair() and self._is_3_of_a_kind()

    def _is_4_of_a_kind(self):
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 4 for value, count in counts.items())

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_royal_flush(self):
        return self.cards[0].value == 10 and self._is_straight() and self._is_flush()

    def __repr__(self):
        return " ".join(str(card) for card in self.cards)

    def __lt__(self, other):
        return self.rank < other.rank
