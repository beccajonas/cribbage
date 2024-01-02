import random
class Round:
    def __init__(self, p1):
        self.p1_cards_played = []
        self.p1_round_points = 0
        self.p2_cards_played = []
        self.p2_round_points = 0
        self.cards_played = []
        self.table_points = 0
        self.dealer = p1  # Set initial dealer

    def update_dealer(self, p1, p2):
        self.dealer = p1 if self.dealer == p2 else p2

    def play(self, p1, p2):
        current_player = p1
        while len(p1.hand.cards) > 0 and len(p2.hand.cards) > 0:
            if self.dealer == p1:
                self.computer_turn(p2)
                if self.table_points == 31:
                    print("31! Table count back to zero.")
                    self.table_points = 0
                    current_player = p2
                    continue
                elif not self.has_valid_card(p1):
                    print("Go! Switching turns.")
                    current_player = p1
                self.player_turn(p1)

            else:
                self.player_turn(p1)
                if self.table_points == 31:
                    print("31! Table count back to zero.")
                    self.table_points = 0
                    current_player = p1
                    continue
                elif not self.has_valid_card(p1):
                    print("Go! Switching turns.")
                    current_player = p1
                self.computer_turn(p2)
        
        while len(p1.hand.cards) > 0 or len(p2.hand.cards) > 0:
            if current_player == p1 and len(p1.hand.cards) > 0:
                self.player_turn(p1)
            elif current_player == p2 and len(p2.hand.cards) > 0:
                self.player_turn(p2)

        while len(p1.hand.cards) > 0:
            self.player_turn(p1)

        while len(p2.hand.cards) > 0:
            self.player_turn(p2)

                
        print("Round over! All cards have been played. Let's score.")


    def computer_turn(self, p):
        print("Computer's turn. ")
        while True:
            index = random.randint(0, len(p.hand.cards) - 1)
            card = p.hand.cards[index]

            if card.points + self.table_points <= 31:
                self.p2_cards_played.append(card)
                self.cards_played.append(card)
                card_points = card.points
                self.table_points += card_points
                print(f">> Computer played: {card} | Table point total: {self.table_points}")
                self.display_cards_played()
                break
            else:
                pass
        
    def player_turn(self, p):
        print(f"Your turn!" )
        input(" --------------------- ")
        self.display_hand(p)
        
        while True:
            input_index = self.get_valid_input(p)
            card = p.hand.cards[input_index]
            
            if card.points + self.table_points <= 31:
                self.p1_cards_played.append(card)
                self.cards_played.append(card)
                self.display_cards_played()
                card_points = card.points
                self.table_points += card_points
                print(f" >> You played {card} | Table point total: {self.table_points}")
                p.hand.cards.pop(input_index)
                input("-----------------------")
                break
            else:
                print("Invalid card. Please choose a card that keeps the total below or equal to 31.")
                self.display_hand(p)


    def calc_points(self, card_list):
        total_points = sum(card.points for card in card_list)
        return total_points 
    
    def has_valid_card(self, p):
        for card in p.hand.cards:
            if card.points + self.table_points <= 31:
                return True
        return False

    def display_hand(self, p):
        print(f"{p.name}'s Hand: {', '.join(str(card) for card in p.hand.cards)}")

    def display_cards_played(self):
        print(f"Cards Played: {', '.join(str(card) for card in self.cards_played)}")

    def display_dealer(self):
        print(f"{self.dealer} is the dealer.")

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

