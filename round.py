import random
import sys

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
        self.go_list = [] #frequency of "Player 1 Go" or frequency of "Player 2 Go" cannot exceed two. When one of them does, it resets

    def play(self):
        while self.has_cards():
            self.player_turn()
            input("-----------")
            self.computer_turn()
            input("-----------")
            self.switch_turns()
        
        if len(self.p2.hand.cards) == 0 and len(self.p1.hand.cards) == 0:
            self.end_round("No cards left to play.")

        elif len(self.p1.hand.cards) == 0:
            print(f"{self.p1.name} has run out of cards.")

            while len(self.p2.hand.cards) > 0:
                self.computer_turn()
                if not self.has_valid_card(self.p2):
                    if len(self.p2.hand.cards) == 0 and len(self.p1.hand.cards) == 0:
                        self.end_round("No cards left to play.")
                    self.reset_table()
                    

        elif len(self.p2.hand.cards) == 0:
            print(f"{self.p2.name} has run out of cards.")

            while len(self.p1.hand.cards) > 0:
                self.player_turn()
                if not self.has_valid_card(self.p1):
                    if len(self.p2.hand.cards) == 0 and len(self.p1.hand.cards) == 0:
                            self.end_round("No cards left to play.")
                    self.reset_table()


        if not self.has_valid_card(self.p1) and not self.has_valid_card(self.p2):
            input("No one can play. Resetting table.")
            self.reset_table()

    def player_turn(self):
        self.check_go_list()
        # Check if the table points reach 31
        if self.table_points == 31:
            print("Table count reaches 31. Resetting count.")
            self.table_points = 0
            self.switch_turns()  

        print(f"{self.p1.name}'s turn!")
        self.display_hand(self.p1)
        input("-----------")
        
        if self.has_valid_card(self.p1):

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
            self.go_list.append("Player 1 Go")
            print(f"{self.p1.name} cannot play. Go!")

    def computer_turn(self):
        self.check_go_list()
        # Check if the table points reach 31
        if self.table_points == 31:
            self.table_points = 0
            self.switch_turns()

        print(f"{self.p2.name}'s turn.")
        input("-----------")

        # Check if the computer has valid cards to play
        if self.has_valid_card(self.p2):
            valid_cards = [card for card in self.p2.hand.cards if card.points + self.table_points <= 31]
    
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
            self.go_list.append("Player 2 Go")
            print(f"{self.p2.name} cannot play. Go!")

    def end_round(self, message):
        input(message)
        print("Round over!")
        sys.exit()
    
    def check_go_list(self):
        for _ in self.go_list:
            if "Player 1 Go" in self.go_list and "Player 2 Go" in self.go_list:
                input("Neither players can go.")
                self.reset_table()
                self.go_list = []
            else:
                pass

    def switch_turns(self):
        if self.turn == self.p1:
            self.turn = self.p2
        elif self.turn == self.p2:
            self.turn = self.p1

    def reset_table(self):
        print("Resetting table points.")
        self.table_points = 0
        self.cards_played = []

    def calc_points(self, card_list):
        return sum(card.points for card in card_list)
    
    def has_cards(self):
        return len(self.p1.hand.cards) > 0 and len(self.p2.hand.cards) > 0
    
    def has_valid_card(self, p):
        # for card in p.hand.cards:
        #     if card.points + self.table_points <= 31:
        #         return True
        # return False
        return any(card.points + self.table_points <= 31 for card in p.hand.cards)

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

