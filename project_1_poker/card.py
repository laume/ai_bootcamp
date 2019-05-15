from colorama import Fore, Style


class Card:
    """
    Single card representation
    """

    suits = ['♠', '♦', '♥', '♣']
    suit_colors = {
        '♠': Fore.WHITE,
        '♦': Fore.BLUE,
        '♥': Fore.RED,
        '♣': Fore.GREEN
    }
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}

    def __init__(self, suit: str, rank: str) -> None:
        """
        Creates and initializes a card
        :param suit: suit of a card
        :param rank: rank of card 2-10, J, Q, K, A
        """
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]

    def __repr__(self) -> str:
        return self.rank + self._colorized_suit

    def __lt__(self, other) -> bool:
        return self.value < other.value

    @property
    def _colorized_suit(self) -> str:
        return Card.suit_colors[self.suit] + self.suit + Style.RESET_ALL
