from card import Card

class Deck:
    def __init__(self):
        self.values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.suits = ["♣", "♥", "♠", "♦"]
        self.cards = self.generate_deck()

    def generate_deck(self):
        deck = []
        for value in self.values:
            for suit in self.suits:
                card = Card(value, suit)
                deck.append(card)
        return deck

    def get_values(self):
        return self.values

    def __str__(self):
        return '\n'.join(map(str, self.cards))
    
    def deal(self, players):
        for _ in range(6): 
            for player in players:
                card = self.cards.pop(0) 
                player.hand.add_card(card)
        
    def remaining_deck(self):
        return self.cards

my_deck = Deck()
print("Initial deck size:", len(my_deck.cards))

print("Remaining deck size:", len(my_deck.remaining_deck()))


