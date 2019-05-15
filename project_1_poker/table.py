import hand_resolver
from hand import Hand
from deck import Deck

class Table:

    ante: int = 10

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

        if self.player.bet(Table.ante):
            self.pot += Table.ante * 2  # 10 from player and 10 from dealer
            self.deal_hands()

    def deal_hands(self):
        # deal player and dealer hands
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        # deal Flop cards
        self.board_cards.append(self.deck.deal_card())
        self.board_cards.append(self.deck.deal_card())
        self.board_cards.append(self.deck.deal_card())

    def player_bets(self) -> None:
        bet_amount = Table.ante * 2
        if self.player.bet(bet_amount):
            self.pot += bet_amount * 2

            # deal Turn and River cards
            self.board_cards.append(self.deck.deal_card())
            self.board_cards.append(self.deck.deal_card())

    def player_folds(self) -> None:
        # do nothing yet
        pass

    def resolve_winner(self):
        best_dealer_hand = hand_resolver.resolve_best_hand(self.dealer_hand + self.board_cards)
        best_player_hand = hand_resolver.resolve_best_hand(self.player_hand + self.board_cards)

        print(f"Best dealer hand: {best_dealer_hand} - {best_dealer_hand.name}")
        print(f"Best player hand: {best_player_hand} - {best_player_hand.name}")

        if best_dealer_hand == best_player_hand:
            self.player.credit(self.pot / 2)
            print("It'a a split!")
        elif best_dealer_hand > best_player_hand:
            print(f"Dealer wins with a {best_dealer_hand.name}!")
        else:
            self.player.credit(self.pot)
            print(f"Player wins {self.pot} with a {best_player_hand.name}. And has total of {self.player.chips}.")

    def __repr__(self) -> str:
        return f"Dealer: \t{self.dealer_hand} \nBoard: \t\t{self.board_cards} \n{self.player.name} \t{self.player_hand}"