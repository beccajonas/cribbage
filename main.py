from termcolor import colored
from deck import Deck
from player import Player
from crib import Crib
from round import Round
from animations import Animations

class Main:
    
    def __init__(self):
        ascii_black = ''' ___   ___   ___
|#  | |A  | |#  | 
| # | | ♠ | | # |
|__#| |__A| |__#|
'''
        ascii_red = ''' ___   ___   ___
|#  | |A  | |#  | 
| # | | ♥ | | # |
|__#| |__A| |__#| 
'''
        print("Welcome to Cribbage!")
        print(colored(ascii_red, "red") + colored(ascii_black, "black"))
        self.deck = Deck()
        self.p1 = Player.create_player()
        self.p2 = Player("Computer")
        self.crib = Crib()
        self.round = Round(self.p1, self.p2)
        self.animations = Animations()

    def fill_crib(self):
        input("Hit enter to shuffle...")
        self.animations.display_shuffle()
        self.deck.shuffle()
        print()
        input("Hit enter to deal...")
        self.animations.display_shuffle()

        self.deck.deal([self.p1, self.p2])
        print()

        while len(self.p1.hand.cards) > 4 or len(self.p2.hand.cards) > 4:
            self.round.display_hand(self.p1)
            self.crib.discard(self.p1)
            self.round.display_hand(self.p1)
            self.crib.discard(self.p1)
            self.crib.computer_discard(self.p2)
            self.crib.computer_discard(self.p2)

        print("The crib is filled. Let's play.")
        input("-------------")

if __name__ == "__main__":
    game = Main()
    game.fill_crib()
    game.round.play()
