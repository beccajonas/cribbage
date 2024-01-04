from deck import Deck
from player import Player
from game_state import GameState
from round import Round

class Main:
    
    def __init__(self):
        ascii_art = ''' ___   ___   ___
|#  | |A  | |#  |
| # | | ♠ | | # |
|__#| |__A| |__#|
'''
        print("Welcome to Cribbage!")
        print(ascii_art)
        self.deck = Deck()
        self.p1 = Player.create_player()
        self.p2 = Player("Computer")
        self.state = GameState()
        self.round = Round(self.p1, self.p2)

    def fill_crib(self):
        input("Shuffling...")
        self.deck.shuffle()
        input("Dealing...")
        self.deck.deal([self.p1, self.p2])

        while len(self.p1.hand.cards) > 4 or len(self.p2.hand.cards) > 4:
            self.round.display_hand(self.p1)
            self.state.discard(self.p1)
            self.round.display_hand(self.p1)
            self.state.computer_discard(self.p2)
            self.state.discard(self.p1)
            self.state.computer_discard(self.p2)

        print("The crib is filled. Let's play.")
        input("---------------")

    def play_round(self):
        self.round.play()

    def score_round(self):
        pass

if __name__ == "__main__":
    game = Main()
    game.fill_crib()
    game.play_round()
