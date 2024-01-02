import random

class GameState:
    def __init__(self, p1, p2):
        self.crib = []
        self.p1_cards_played = []
        self.p2_cards_played = []
        self.cards_played = []
        self.dealer = p1  # Set initial dealer

    def update_dealer(self, p1, p2):
        self.dealer = p1 if self.dealer == p2 else p2

    def discard(self, p1):
        index1 = int(input("Select the number of a card you want to discard. (1 for 1st card in hand, 2 for 2nd, etc.) >> "))
        index1 -= 1 
        self.crib.append(p1.hand.cards[index1])
        p1.hand.discard(index1)
        
    def computer_discard1(self, p2):
        crib_card1 = random.randint(0, 5)
        self.crib.append(p2.hand.cards[crib_card1])
        p2.hand.discard(crib_card1)

    def computer_discard2(self, p2):
        crib_card2 = random.randint(0, 4)
        self.crib.append(p2.hand.cards[crib_card2])
        p2.hand.discard(crib_card2)