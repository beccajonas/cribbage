import random
class Round:
    def __init__(self, p1, p2):
        self.p1 = p1 #person
        self.p2 = p2 #computer
        self.turn = p1 #person goes first
        self.p1_cards_played = []
        self.p1_round_points = 0
        self.p2_cards_played = []
        self.p2_round_points = 0
        self.cards_played = [] #combination of both players cards played
        self.table_points = 0 #can never exceed 31
        self.go_check = [] #frequency of "Player 1 Go" or frequency of "Player 2 Go" cannot exceed two. When one of them does, it resets

    def play(self):
        input("Checking go count (Line 16)")
        if self.go_check >= 2:
            input(f"Go count is {self.go_check} (Line 18)")
            self.reset_round()
            input(f"Reset round (line 20)")
            self.go_check = 0
        input(f"Go count is {self.go_check} (Line 22)")

        while self.has_cards():
            self.player_turn()
            
            input("Checking go count (Line 27)")
            if self.go_check >= 2:
                input(f"Go count is {self.go_check} (Line 29)")
                self.reset_round()
                input(f"Reset round (line 31)")
                self.go_check = 0
            input(f"Go count is {self.go_check} (Line 33)")

            input("-----line 18----------")
            self.computer_turn()

            input("Checking go count (Line 38)")
            if self.go_check >= 2:
                input(f"Go count is {self.go_check} (Line 40)")
                self.reset_round()
                input(f"Reset round (line 42)")
                self.go_check = 0
            input(f"Go count is {self.go_check} (Line 44)")

            input("-----line 46----------")
            self.switch_turns()
            input("-----line 48----------")
        
        if len(self.p2.hand.cards) == 0 and len(self.p1.hand.cards) == 0:
            input("No cards are left")
            print("Round over")
        elif len(self.p1.hand.cards) == 0:
            print(f"{self.p1.name} has run out of cards.")
            while len(self.p2.hand.cards) > 0:
                self.computer_turn()
        elif len(self.p2.hand.cards) == 0:
            print(f"{self.p2.name} has run out of cards.")
            while len(self.p1.hand.cards) > 0:
                self.player_turn()

        if not self.has_valid_card(self.p1) and not self.has_valid_card(self.p2):
            input("No cards are valid")
            self.reset_round()

    def player_turn(self):
        print(f"{self.p1.name}'s turn!")
        self.display_hand(self.p1)
        input(f"------{self.p1.name}'s turn!-------")

        # Check if the table points reach 31
        input("Checking if self.table_points is 31 (Line 72)")
        if self.table_points == 31:
            print("Table count reaches 31. Resetting count.")
            self.table_points = 0
            input("Switching turns (line 76)") 
            self.switch_turns()  
        input("Self.table_points is not 31 (Line 78)")  
        
        input("Checking for valid card")
        if self.has_valid_card(self.p1):
            input("Valid card exists")

            valid_input = False
            while not valid_input:
                input_index = self.get_valid_input(self.p1)

                if input_index is not None:  # Check if get_valid_input returns a valid index
                    chosen_card = self.p1.hand.cards[input_index]

                    if chosen_card.points + self.table_points <= 31:
                        valid_input = True
                        self.p1.hand.cards.pop(input_index)  # Remove the card only if it's valid
                        self.cards_played.append(chosen_card)
                        self.table_points += chosen_card.points
                        print(f"{self.p1.name} plays {chosen_card}. | Table count = {self.table_points}")
                        self.switch_turns()
                    else:
                        print("Invalid move. The selected card exceeds 31 points. Try again.")
                else:
                    print("Invalid input. Please enter a valid card position.")        

        else:
            self.go_check += 1
            print(f"Go check = {self.go_check} (Line 105)")
            print(f"{self.p1.name} cannot play. Go! (Line 106)")

    def computer_turn(self):
        print(f"{self.p2.name}'s turn.")
        self.display_hand(self.p2)
        input(f"------{self.p2.name}'s turn!-------")

        # Check if the table points reach 31
        input("Checking if self.table_points is 31 (Line 114)")
        if self.table_points == 31:
            print("Table count reaches 31. Resetting count.")
            self.table_points = 0
            input("Switching turns (line 118)") 
            self.switch_turns()
        input("Self.table_points is not 31 (Line 120)")  

        # Check if the computer has valid cards to play
        input("Checking for valid card")
        if self.has_valid_card(self.p2):
            valid_cards = [card for card in self.p2.hand.cards if card.points + self.table_points <= 31]
            input("Valid card exists")
    
            if valid_cards:
                # If the computer has valid cards, it plays one randomly
                chosen_card = random.choice(valid_cards)
                self.p2.hand.cards.remove(chosen_card)
                self.cards_played.append(chosen_card)
                self.table_points += chosen_card.points

                print(f"{self.p2.name} plays {chosen_card}.")

            # Display the updated game state
            self.display_hand(self.p2)
            self.display_cards_played()
            print(f"Table Points: {self.table_points}")

        else:
            # If the computer has no valid cards, it says "Go"
            self.go_check += 1
            print(f"Go check = {self.go_check} (Line 145)")
            print(f"{self.p2.name} cannot play. Go! (Line 146)")
                

    def switch_turns(self):
        if self.turn == self.p1:
            self.turn = self.p2
        elif self.turn == self.p2:
            self.turn = self.p1

    def reset_round(self):
        print("Resetting round.")
        self.table_points = 0
        self.cards_played = []

    def calc_points(self, card_list):
        total_points = sum(card.points for card in card_list)
        return total_points 
    
    def has_cards(self):
        return len(self.p1.hand.cards) > 0 and len(self.p2.hand.cards) > 0
    
    def has_valid_card(self, p):
        for card in p.hand.cards:
            if card.points + self.table_points <= 31:
                return True
        return False

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

