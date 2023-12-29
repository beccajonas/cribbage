from deck import Deck
from player import Player
import random

class Main:
    def __init__(self):
        self.deck = Deck()
        self.crib = []
        self.player1_name = input("Enter Player 1's name: ")
        self.player1 = Player(is_dealer=False, name=self.player1_name)
        self.player2 = Player(is_dealer=True, name="Computer")

    def start_game(self):
        print("Welcome to Cribbage!")
        
        random.shuffle(self.deck.cards)

        self.deck.deal([self.player1, self.player2])

        self.display_hands()
        index1 = int(input("Select the number of a card you want to discard. (1 for 1st card in hand, 2 for 2nd, etc.) >> "))
        index1 -= 1  # Adjust for 0-based indexing
        self.crib.append(self.player1.hand.cards[index1])
        self.player1.hand.discard(index1)
        self.display_hands()
        print("Crib:", [str(card) for card in self.crib])

        crib_card1 = random.randint(0, 5)
        self.crib.append(self.player2.hand.cards[crib_card1])
        self.player2.hand.discard(crib_card1)
        print("Crib:", [str(card) for card in self.crib])
        
        index2 = int(input("Select second card you'd like to discard >> "))
        index2 -= 1  # Adjust for 0-based indexing
        self.crib.append(self.player1.hand.cards[index2])
        self.player1.hand.discard(index2)
        print("Crib:", [str(card) for card in self.crib])

        crib_card2 = random.randint(0, 4)
        self.crib.append(self.player2.hand.cards[crib_card2])
        self.player2.hand.discard(crib_card2)
        
        self.display_hands()
        # Implement the rest of your game logic here
        print("Crib:", [str(card) for card in self.crib])

    def display_hands(self):
        for player in [self.player1]:
            print(f"{player.name}'s Hand:")
            print(player.hand)

if __name__ == "__main__":
    game = Main()
    game.start_game()
