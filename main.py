from deck import Deck
from player import Player
import random

class Main:
    def __init__(self):
        self.deck = Deck()
        self.crib = []

        self.p1_name = input("Enter Player 1's name: ")
        self.p1 = Player(self.p1_name)
        self.p2 = Player("Computer")
        self.is_computer_dealer = True

        self.p1_cards_played = []
        self.p2_cards_played = []

        self.cards_played = []

    def start_round(self):
        print("Welcome to Cribbage!")
        
        random.shuffle(self.deck.cards)

        self.deck.deal([self.p1, self.p2])

        while len(self.p1.hand.cards) > 0 or len(self.p2.hand.cards) > 0:
            self.display_hand(self.p1)
            index1 = int(input("Select the number of a card you want to discard. (1 for 1st card in hand, 2 for 2nd, etc.) >> "))
            index1 -= 1 
            self.crib.append(self.p1.hand.cards[index1])
            self.p1.hand.discard(index1)
            self.display_hand(self.p1)

            crib_card1 = random.randint(0, 5)
            self.crib.append(self.p2.hand.cards[crib_card1])
            self.p2.hand.discard(crib_card1)
            
            index2 = int(input("Select second card you'd like to discard >> "))
            index2 -= 1 
            self.crib.append(self.p1.hand.cards[index2])
            self.p1.hand.discard(index2)

            crib_card2 = random.randint(0, 4)
            self.crib.append(self.p2.hand.cards[crib_card2])
            self.p2.hand.discard(crib_card2)
            
            self.play_round()

        print("Round over! All cards have been played.")
        self.start_round()

    def display_hand(self, player):
        print(f"{player.name}'s Hand: {', '.join(str(card) for card in player.hand.cards)}")

    def display_cards_played(self):
        print(f"Cards Played: {', '.join(str(card) for card in self.cards_played)}")

    def play_round(self):
        while len(self.p1.hand.cards) > 0 and len(self.p2.hand.cards) > 0:
            if self.is_computer_dealer:
                self.non_dealer_round()
            else:
                self.dealer_round()
            self.is_computer_dealer = not self.is_computer_dealer

        print("Round over! All cards have been played. Let's score.")

    def dealer_round(self):
        print("Computer's turn. ")
        p2_index = random.randint(0, len(self.p2.hand.cards) - 1)
        card = self.p2.hand.cards.pop(p2_index)
        self.p2_cards_played.append(card)
        self.cards_played.append(card)
        print(f">> Computer played: {card}")

        self.display_cards_played()

        print(f"{self.p1_name}'s turn! >>" )
        self.display_hand(self.p1)
        p1_index = int(input("Select the number of a card you want to play >> "))
        p1_index -= 1
        card = self.p1.hand.cards.pop(p1_index)
        self.p1_cards_played.append(card)
        self.cards_played.append(card)
        print(f" >> You played {card} ")
        
        self.display_cards_played()

    def non_dealer_round(self):
        print("Your turn! ")

        self.display_hand(self.p1)
        p1_index = int(input("Select the number of a card you want to play >> "))
        p1_index -= 1 
        card = self.p1.hand.cards.pop(p1_index)
        self.p1_cards_played.append(card)
        self.cards_played.append(card)
        print(f" >> You played {card} ")

        self.display_cards_played()

if __name__ == "__main__":
    game = Main()
    game.start_round()
