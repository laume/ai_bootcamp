import random

suits = ['♠', '♦', '♥', '♣']
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

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

class Table:

	def __init__(self):
		self.pot = 0

	def new_game(self):
		self.pot = 0
		self.deck = Deck()
		self.deck.shuffle()

deck = Deck()
deck.shuffle()

print(deck.deck)

