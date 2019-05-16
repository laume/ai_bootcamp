from typing import List

from card import Card

CARD = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}    │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

HIDDEN_CARD = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""


def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))


def ascii_version_of_card(cards: List[Card]) -> str:
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """

    def card_to_string(card: Card) -> str:
        # 10 is the only card with a 2-char rank abbreviation
        # rank = card.rank if card.rank == '10' else card.rank[0]

        # add the individual card on a line by line basis
        return CARD.format(rank=card.rank, suit=card.colorized_suit)

    return join_lines(map(card_to_string, cards))


def ascii_version_of_hidden_card(cards: List[Card]):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """

    return join_lines((HIDDEN_CARD, ascii_version_of_card(cards[1:])))
