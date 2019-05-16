from typing import Tuple, List

import card_printer
import hand_resolver
import time

from card import Card
from hand import Hand
from deck import Deck
from player import Player


class Table:
    ante: int = 10

    def __init__(self, player):
        self.pot = 0
        self.player_hand = []
        self.dealer_hand: List[Card] = []
        self.community_cards: List[Card] = []
        self.deck = Deck()
        self.player = player
        self.dealer = Player("Dealer", 0)

        print(f"Player {self.player.name} joined the table!")

    def new_game(self):
        self.deck = Deck()
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.community_cards.clear()
        self.pot = 0
        self.deck.shuffle()

        if self.player.bet(Table.ante):
            self.pot += Table.ante * 2  # 10 from player and 10 from dealer
            self.deal_hands()

    def deal_hands(self):
        # deal player and dealer hands
        card = self.deck.deal_card()
        card.hidden = True
        self.dealer_hand.append(card)
        self.dealer_hand.append(self.deck.deal_card())

        self.player_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())

        # deal Flop cards
        self.community_cards.append(self.deck.deal_card())
        self.community_cards.append(self.deck.deal_card())
        self.community_cards.append(self.deck.deal_card())

    def player_bets(self) -> None:
        bet_amount = Table.ante * 2
        if self.player.bet(bet_amount):
            self.pot += bet_amount * 2
            time.sleep(1)

    def draw_turn_card(self) -> None:
        turn_card = self.deck.deal_card()
        self.community_cards.append(turn_card)

    def draw_river_card(self) -> None:
        river_card = self.deck.deal_card()
        self.community_cards.append(river_card)

    def player_folds(self) -> None:
        # do nothing yet
        pass

    def resolve_winner(self):
        for card in self.dealer_hand:
            card.hidden = False

        best_dealer_hand = hand_resolver.resolve_best_hand(self.dealer_hand + self.community_cards)
        best_player_hand = hand_resolver.resolve_best_hand(self.player_hand + self.community_cards)

        print(f"Best dealer hand: {best_dealer_hand} - {best_dealer_hand.name}")
        print(f"Best player hand: {best_player_hand} - {best_player_hand.name}")

        if best_dealer_hand.score == best_player_hand.score:
            self.player.credit(self.pot / 2)
            print("It'a a split!")
        elif best_dealer_hand.score > best_player_hand.score:
            print(f"Dealer wins with a {best_dealer_hand.name}!")
        else:
            self.player.credit(self.pot)
            print(f"Player wins {self.pot} with a {best_player_hand.name}. And has total of {self.player.chips}.")

    def dealer_qualifies(self) -> bool:
        if hand_resolver.is_pair_of_4_or_better(self.dealer_hand + self.community_cards):
            return True
        else:
            self.player.credit(self.pot)
            print("Dealer folds. Player wins.")
            return False

    def print_table(self) -> None:
        print("Dealer:")
        print(card_printer.ascii_version_of_hidden_card(self.dealer_hand))

        print("Board")
        print(card_printer.ascii_version_of_card(self.community_cards))

        print(f"{self.player.name}:")
        print(card_printer.ascii_version_of_card(self.player_hand))

