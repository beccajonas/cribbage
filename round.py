import random
class Round:
    def __init__(self, p1, p2):
        self.p1_cards_played = []
        self.p2_cards_played = []
        self.cards_played = []
        self.dealer = p1  # Set initial dealer

    def update_dealer(self, p1, p2):
        self.dealer = p1 if self.dealer == p2 else p2

    def play(self, p1, p2):
        while len(p1.hand.cards) > 0 and len(p2.hand.cards) > 0:
            if self.dealer == p1:
                print("Computer's turn. ")
                index = random.randint(0, len(p2.hand.cards) - 1)
                card = p2.hand.cards.pop(index)
                self.p2_cards_played.append(card)
                self.cards_played.append(card)
                print(f">> Computer played: {card}")
                self.display_cards_played()

                print(f"Your turn! >>" )
                self.display_hand(p1)
                input_index = self.get_valid_input(p1)
                card = p1.hand.cards.pop(input_index)
                self.p1_cards_played.append(card)
                self.cards_played.append(card)
                print(f" >> You played {card} ")
            
            else:
                print(f"Your turn! >>" )
                self.display_hand(p1)
                input_index = self.get_valid_input(p1)
                card = p1.hand.cards.pop(input_index)
                self.p1_cards_played.append(card)
                self.cards_played.append(card)
                print(f" >> You played {card} ")
                self.display_cards_played()

                print("Computer's turn. ")
                index = random.randint(0, len(p2.hand.cards) - 1)
                card = p2.hand.cards.pop(index)
                self.p2_cards_played.append(card)
                self.cards_played.append(card)
                print(f">> Computer played: {card}")
                
        print("Round over! All cards have been played. Let's score.")
        
    def display_hand(self, p):
        print(f"{p.name}'s Hand: {', '.join(str(card) for card in p.hand.cards)}")

    def display_cards_played(self):
        print(f"Cards Played: {', '.join(str(card) for card in self.cards_played)}")

    def get_valid_input(self, p):
        while True:
            input_index_string = input("Select the number of a card you want to play >> ")
            if input_index_string.isdigit():
                input_index = int(input_index_string) - 1
                if input_index in range(0, len(p.hand.cards)):
                    return input_index
                else:
                    print("Invalid input. Please enter a valid card position.")
            else: print("Invalid input. Please enter a valid card position.")

