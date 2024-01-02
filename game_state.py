class GameState:
    def __init__(self, p1, p2):
        self.crib = []
        self.p1_cards_played = []
        self.p2_cards_played = []
        self.cards_played = []
        self.dealer = p1  # Set initial dealer

    def update_dealer(self, p1, p2):
        self.dealer = p1 if self.dealer == p2 else p2
