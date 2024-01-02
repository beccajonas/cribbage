from deck import Deck
from player import Player
from game_state import GameState
import random

class Main:
    def __init__(self):
        print("Welcome to Cribbage!")
        self.deck = Deck()
        self.p1 = Player.create_player_with_input()
        self.p2 = Player("Computer")
        self.state = GameState(self.p1, self.p2)
        self.state.dealer = self.p1

    def start_round(self):
        self.state.update_dealer(self.p1, self.p2)
        self.deck.shuffle()
        self.deck.deal([self.p1, self.p2])

        while len(self.p1.hand.cards) > 0 or len(self.p2.hand.cards) > 0:
            self.display_hand(self.p1)
            self.state.discard(self.p1)
            self.display_hand(self.p1)
            self.state.computer_discard1(self.p2)
            self.state.discard(self.p1)
            self.state.computer_discard2(self.p2)
            
            self.play_round()

        print("Round over! All cards have been played.")
        self.start_round()

    def display_hand(self, player):
        print(f"{player.name}'s Hand: {', '.join(str(card) for card in player.hand.cards)}")

    def display_cards_played(self):
        print(f"Cards Played: {', '.join(str(card) for card in self.state.cards_played)}")

    def play_round(self):
        while len(self.p1.hand.cards) > 0 and len(self.p2.hand.cards) > 0:
            if self.state.dealer:
                self.non_dealer_round()
            else:
                self.dealer_round()
            self.state.dealer = not self.state.dealer

        print("Round over! All cards have been played. Let's score.")

    def dealer_round(self):
        print("Computer's turn. ")
        p2_index = random.randint(0, len(self.p2.hand.cards) - 1)
        card = self.p2.hand.cards.pop(p2_index)
        self.state.p2_cards_played.append(card)
        self.state.cards_played.append(card)
        print(f">> Computer played: {card}")

        self.display_cards_played()

        print(f"{self.p1.name}'s turn! >>" )
        self.display_hand(self.p1)
        p1_index = int(input("Select the number of a card you want to play >> "))
        p1_index -= 1
        card = self.p1.hand.cards.pop(p1_index)
        self.state.p1_cards_played.append(card)
        self.state.cards_played.append(card)
        print(f" >> You played {card} ")
        
        self.display_cards_played()

    def non_dealer_round(self):
        print("Your turn! ")

        self.display_hand(self.p1)
        p1_index = int(input("Select the number of a card you want to play >> "))
        p1_index -= 1 
        card = self.p1.hand.cards.pop(p1_index)
        self.state.p1_cards_played.append(card)
        self.state.cards_played.append(card)
        print(f" >> You played {card} ")

        self.display_cards_played()

if __name__ == "__main__":
    game = Main()
    game.start_round()
