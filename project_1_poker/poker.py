import itertools
from hand import Hand
from deck import Deck


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

        print(f"Best dealer hand: {best_dealer_hand} - {best_dealer_hand.name()}")
        print(f"Best player hand: {best_player_hand} - {best_player_hand.name()}")

        if best_dealer_hand == best_player_hand:
            print("Split")
        elif best_dealer_hand > best_player_hand:
            print(f"Dealer wins with a {best_dealer_hand.name()}!")
        else:
            print(f"Player wins with a {best_player_hand.name()}")

    # TODO resolving hands without best kicker for now
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
