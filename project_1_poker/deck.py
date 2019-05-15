from card import Card
import random


class Deck:

    def __init__(self) -> None:
        """
        Creates a full deck of cards
        """
        self.deck = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self) -> None:
        """
        Shuffle deck cards
        """
        random.shuffle(self.deck)

    def deal_card(self) -> Card:
        """
        Get a card from the deck
        :return: a card
        """
        return self.deck.pop()
