from deck import Deck


class Card:
    """
    Single card representation
    """

    def __init__(self, suit: str, rank: str) -> None:
        """
        Creates and initializes a card
        :param suit: suit of a card
        :param rank: rank of card 2-10, J, Q, K, A
        """
        self.suit = suit
        self.rank = rank
        self.value = Deck.values[rank]

    def __repr__(self) -> str:
        return self.rank + self.suit[0]

    def __lt__(self, other) -> bool:
        return self.value < other.value
