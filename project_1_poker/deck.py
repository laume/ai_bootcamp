from card import Card
import random


class Deck:
    suits = ['♠', '♦', '♥', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}

    def __init__(self) -> None:
        """
        Creates a full deck of cards
        """
        self.deck = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]

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
