import hand_resolver
from card import Card


def test_better_than_pair_of_4_yes():
    cards = [Card.of('4S'), Card.of('4D'), Card.of('6S'), Card.of('7D'), Card.of('AS')]

    assert hand_resolver.is_pair_of_4_or_better(cards)


def test_better_than_pair_of_4_no():
    cards = [Card.of('3S'), Card.of('3D'), Card.of('6S'), Card.of('7D'), Card.of('AS')]

    assert not hand_resolver.is_pair_of_4_or_better(cards)