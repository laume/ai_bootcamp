import random
import itertools

suits = ['♠', '♦', '♥', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
ante = 10

class Card:
	
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __repr__(self):
		return self.rank + self.suit[0]

class Deck:
	
	def __init__(self):
		self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

	def shuffle(self):
		random.shuffle(self.deck)

	def deal_card(self):
		return self.deck.pop()

class Hand:

	def __init__(self,cards):
		self.cards = cards

	def combination(self):
		if self.is_flush():
			return "Flush! {}".format(self.cards)
		if self.is_3_of_a_kind():
			return "Three of a kind! {}".format(self.cards)
		if self.is_pair():
			return "Pair! {}".format(self.cards)
		else:
			return 'dud'

	def __repr__(self):
		return " ".join(str(card) for card in self.cards)

	def is_pair(self):
		ranks = list(map(lambda card: card.rank, self.cards))
		counts = dict((rank, ranks.count(rank)) for rank in ranks)
		return any(count == 2 for value, count in counts.items())

	def is_3_of_a_kind(self):
		ranks = list(map(lambda card: card.rank, self.cards))
		counts = dict((rank, ranks.count(rank)) for rank in ranks)
		return any(count == 3 for value, count in counts.items())

	def is_straight(self):
		pass

	def is_flush(self):
		return len(set(map(lambda card: card.suit, self.cards))) == 1

	def is_full_house(self):
		pass

	def is_4_of_a_kind(self):
		pass

	def is_straight_flush(self):
		pass

	def is_royal_flush(self):
		pass


class Player:

	def __init__(self,name):
		self.chips = 100
		self.name = name

	def bet(self,amount):
		if amount > self.chips:
			 print("Sorry, your bet can't exceed",chips.total)
			 return False
		else:
			self.chips -= amount
			print("{} has {} chips remaining".format(self.name,self.chips))
			return True

class Table:

	def __init__(self):
		self.pot = 0

	def new_game(self,player):
		self.pot = 0
		self.deck = Deck()
		self.deck.shuffle()

		self.player = player
		
		# if self.player.bet(10):
			# self.pot += 10 * 2

		self.deal_hands()

	def deal_hands(self):
		self.player_hand = []
		self.dealer_hand = []
		self.board_cards = []

		self.player_hand.append(self.deck.deal_card())
		self.dealer_hand.append(self.deck.deal_card())

		self.player_hand.append(self.deck.deal_card())
		self.dealer_hand.append(self.deck.deal_card())

		self.board_cards.append(self.deck.deal_card())
		self.board_cards.append(self.deck.deal_card())
		self.board_cards.append(self.deck.deal_card())
		self.board_cards.append(self.deck.deal_card())
		self.board_cards.append(self.deck.deal_card())


iteration = 0
playing = True

table = Table()
# table.new_game(Player("Martynas"))

while playing:
	table.new_game(Player("Martynas"))
	a = table.player_hand + table.board_cards

	hands = [Hand(cards) for cards in itertools.combinations(a, 5)]

	for hand in hands:
		if hand.is_flush():
			print("{} after {} iterations".format(hand, iteration))
			playing = False

	iteration += 1


# print("Current pot is ", table.pot)
# print("--------------")
# print("Player hand: ", table.player_hand)
# print("On the table: ", table.board_cards)

# a = table.player_hand + table.board_cards

# hands = [Hand(cards) for cards in itertools.combinations(a, 5)]

# for hand in hands:
	# print(hand.combination())
