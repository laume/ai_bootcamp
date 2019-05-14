class Hand:
    def __init__(self, cards):
        self.cards = sorted(list(cards))

    def combination(self):
        if self.is_royal_flush():
            return 1000, "Royal Flush"
        if self.is_straight_flush():
            return 900, "Straight flush"
        if self.is_4_of_a_kind():
            return 800, "Four of a kind"
        if self.is_full_house():
            return 700, "Full house"
        if self.is_flush():
            return 600, "Flush"
        if self.is_straight():
            return 500, "Straight"
        if self.is_3_of_a_kind():
            return 400, "Three of a kind"
        if self.is_pair():
            return 300, "Pair"
        else:
            return max(self.cards).value, "High card"

    def name(self):
        return self.combination()[1]

    def is_pair(self):
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 2 for value, count in counts.items())

    def is_3_of_a_kind(self):
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 3 for value, count in counts.items())

    def is_straight(self):
        return all(x.value == y.value - 1 for x, y in zip(self.cards, self.cards[1:]))

    def is_flush(self):
        return len(set(map(lambda card: card.suit, self.cards))) == 1

    def is_full_house(self):
        return self.is_pair() and self.is_3_of_a_kind()

    def is_4_of_a_kind(self):
        ranks = list(map(lambda card: card.rank, self.cards))
        counts = dict((rank, ranks.count(rank)) for rank in ranks)
        return any(count == 4 for value, count in counts.items())

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_royal_flush(self):
        return self.cards[0].value == 10 and self.is_straight() and self.is_flush()

    def __repr__(self):
        return " ".join(str(card) for card in self.cards)

    def __lt__(self, other):
        return self.combination()[0] < other.combination()[0]