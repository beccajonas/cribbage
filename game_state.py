import random

class GameState:
    def __init__(self):
        self.crib = []

    def discard(self, p):
        input_index = self.get_valid_input(p)
        self.crib.append(p.hand.cards[input_index])
        p.hand.discard(input_index)
        
    def computer_discard(self, p):
        hand_length = len(p.hand.cards)
        if hand_length > 0:
            crib_card = random.randint(0, hand_length - 1)
        self.crib.append(p.hand.cards[crib_card])
        p.hand.discard(crib_card)

    def get_valid_input(self, p):
        while True:
            input_index_string = input("Select the number of a card you want to put into crib. (1 for 1st card in hand, 2 for 2nd, etc.) >> ")
            if input_index_string.isdigit():
                input_index = int(input_index_string) - 1
                if input_index in range(0, len(p.hand.cards)):
                    return input_index
                else:
                    print("Invalid input. Please enter a valid card position.")
            else: print("Invalid input. Please enter a valid card position.")