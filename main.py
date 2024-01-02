from deck import Deck
from player import Player
from game_state import GameState
from round import Round

class Main:
    def __init__(self):
        print("Welcome to Cribbage!")
        self.deck = Deck()
        self.p1 = Player.create_player()
        self.p2 = Player("Computer")
        self.state = GameState()
        self.round = Round(self.p1, self.p2)

    def fill_crib(self):
        self.deck.shuffle()
        self.deck.deal([self.p1, self.p2])
        self.round.display_dealer()

        while len(self.p1.hand.cards) > 4 or len(self.p2.hand.cards) > 4:
            self.display_hand(self.p1)
            self.state.discard(self.p1)
            self.display_hand(self.p1)
            self.state.computer_discard(self.p2)
            self.state.discard(self.p1)
            self.state.computer_discard(self.p2)

        print("The crib is filled. Let's play.")

    def play_round(self):
        self.round.play(self.p1, self.p2)
        self.round.update_dealer(self.p1, self.p2)

    def display_hand(self, p):
        print(f"{p.name}'s Hand: {', '.join(str(card) for card in p.hand.cards)}")

    def display_cards_played(self):
        print(f"Cards Played: {', '.join(str(card) for card in self.round.cards_played)}")

if __name__ == "__main__":
    game = Main()
    game.fill_crib()
    game.play_round()
