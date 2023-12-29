class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        if not self.cards:
            return "Empty Hand"

        hand_str = ", ".join(str(card) for card in self.cards)
        return hand_str
    
    def discard(self, index):
        self.cards.pop(index)