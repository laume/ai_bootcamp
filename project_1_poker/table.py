from typing import List

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
        self.ante = 0
        self.player_bet = 0
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
        self.ante = 0
        self.player_bet = 0
        self.deck.shuffle()

        if self.player.bet(Table.ante):
            self.ante = Table.ante
            self.deal_hands()
            print(f"New game. Ante is {self.ante}")

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
            self.player_bet = bet_amount
            print(f"{self.player.name} bets {self.player_bet}")
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
        best_dealer_hand = hand_resolver.resolve_best_hand(self.dealer_hand + self.community_cards)
        best_player_hand = hand_resolver.resolve_best_hand(self.player_hand + self.community_cards)

        if not hand_resolver.is_pair_of_4_or_better(best_dealer_hand):
            #  player gets his bet back and Ante PayOff
            ante_payoff = Table.win_amount(best_player_hand, self.ante)
            self.player.credit(ante_payoff + self.player_bet)
            print(f"Dealer folds. Player wins {ante_payoff}")
        else:
            for card in self.dealer_hand:
                card.hidden = False

            self.check_winner(best_dealer_hand, best_player_hand)

    def check_winner(self, dealer_hand: Hand, player_hand: Hand):
        print(f"Best dealer hand: {dealer_hand} - {dealer_hand.name}")
        print(f"Best player hand: {player_hand} - {player_hand.name}")

        if dealer_hand.score == player_hand.score:
            self.player.credit(self.ante + self.player_bet)
            print("It'a a split!")
        elif dealer_hand.score > player_hand.score:
            print(f"Dealer wins with a {player_hand.name}!")
        else:
            win_amount = Table.win_amount(player_hand, self.ante) + (self.player_bet * 2)
            self.player.credit(win_amount)
            print(f"Player wins {win_amount} with a {player_hand.name}. And has total of {self.player.chips}.")

    def print_table(self, show_dealer_card: bool = False) -> None:
        print("Dealer:")
        if show_dealer_card:
            print(card_printer.ascii_version_of_card(self.dealer_hand))
        else:
            print(card_printer.ascii_version_of_hidden_card(self.dealer_hand))

        print("Board")
        print(card_printer.ascii_version_of_card(self.community_cards))

        print(f"{self.player.name}:")
        print(card_printer.ascii_version_of_card(self.player_hand))

    @staticmethod
    def win_amount(hand: Hand, bet_amount: int) -> int:
        """
        Determines win amount based on Ante Table
        :param hand: winning hand
        :param bet_amount: player bet amount
        """

        if hand.is_royal_flush():
            return bet_amount * 100
        elif hand.is_straight_flush():
            return bet_amount * 20
        elif hand.is_4_of_a_kind():
            return bet_amount * 10
        elif hand.is_full_house():
            return bet_amount * 3
        elif hand.is_flush():
            return bet_amount * 2
        else:
            return bet_amount
