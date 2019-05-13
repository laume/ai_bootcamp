import random
import itertools

suits = ['♠', '♦', '♥', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
ante = 10


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __repr__(self):
        return self.rank + self.suit[0]

    def __lt__(self, other):
        return self.value < other.value


class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


class Hand:
    def __init__(self, cards):
        self.cards = sorted(list(cards))

    def combination(self):
        if self.is_royal_flush():
            return 100
        if self.is_straight_flush():
            return 90
        if self.is_full_house():
            return 80
        if self.is_flush():
            return 70
        if self.is_straight():
            return 60
        if self.is_3_of_a_kind():
            return 50
        if self.is_pair():
            return 40
        else:
            return 30

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
        return self.combination() < other.combination()


class Player:

    def __init__(self, name):
        self.chips = 100
        self.name = name

    def bet(self, amount):
        if amount > self.chips:
            print("Sorry, your bet can't exceed", self.chips)
            return False
        else:
            self.chips -= amount
            print("{} has {} chips remaining".format(self.name, self.chips))
            return True


class Table:

    def __init__(self, player):
        self.pot = 0
        self.player_hand = []
        self.dealer_hand = []
        self.board_cards = []
        self.deck = Deck()
        self.player = player

    def new_game(self):
        self.deck = Deck()
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.board_cards.clear()
        self.pot = 0
        self.deck.shuffle()

        if self.player.bet(10):
            self.pot += 10 * 2
            self.deal_hands()

    def deal_hands(self):
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        self.board_cards.append(self.deck.deal_card())
        self.board_cards.append(self.deck.deal_card())
        self.board_cards.append(self.deck.deal_card())
        self.board_cards.append(self.deck.deal_card())
        self.board_cards.append(self.deck.deal_card())

    def resolve_hands(self):
        best_dealer_hand = self.best_hand(table.dealer_hand + table.board_cards)
        best_player_hand = self.best_hand(table.player_hand + table.board_cards)

        print(best_dealer_hand)
        print(best_player_hand)

        if best_dealer_hand > best_player_hand:
            print("Dealer wins!")
        else:
            print("Player wins!")

    # TODO resolving hands without best kicker
    def best_hand(self, cards):
        return max([Hand(cards) for cards in itertools.combinations(cards, 5)])


iteration = 0
playing = True

p1 = Player("Martynas")
table = Table(p1)

while playing:
    table.new_game()

    table.resolve_hands()

    playing = False

# print("Current pot is ", table.pot)
# print("--------------")
# print("Player hand: ", table.player_hand)
# print("On the table: ", table.board_cards)

# a = table.player_hand + table.board_cards

# hands = [Hand(cards) for cards in itertools.combinations(a, 5)]

# for hand in hands:
# print(hand.combination())
