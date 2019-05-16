from card import Card
from hand import Hand


def test_two_pair():
    cards = (Card.of('4S'), Card.of('4D'), Card.of('5S'), Card.of('5D'), Card.of('AS'))
    hand = Hand(cards)

    assert not hand.is_two_pair()
