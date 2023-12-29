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

        p1_cards_played = []
        p2_cards_played = []

        cards_played = []
        

    def start_game(self):
        print("Welcome to Cribbage!")
        
        random.shuffle(self.deck.cards)

        self.deck.deal([self.p1, self.p2])

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
        
        self.display_hand(self.p1)
        self.dealer_round()
        

    def display_hand(self, player):
        print(f"{player.name}'s Hand:")
        print(player.hand)

    def dealer_round(self):
        print("Let's play! You dealt. So Computer goes first...")
        

if __name__ == "__main__":
    game = Main()
    game.start_game()
