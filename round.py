from scoring import Scoring
import random
import time
import sys

class Round:
    def __init__(self, p1, p2):
        self.p1 = p1 
        self.p2 = p2 # Computer player
        self.turn = p1 # Person who goes first
        self.p1_cards_played = []
        self.p1_round_points = 0
        self.p2_cards_played = []
        self.p2_round_points = 0
        self.cards_played = [] # Combination of both players cards played
        self.table_points = 0 
        self.go_list = [] #Frequency of "Player 1 Go" or frequency of "Player 2 Go" cannot exceed 1. When one of them does, it resets
        self.scoring = Scoring()

    def play(self):
        while self.has_cards():
            print(f"{self.p1.name}'s points = {self.p1_round_points} | Computer's points = {self.p2_round_points}")
            self.player_turn()
            self.computer_turn()
            self.switch_turns()
        
        if len(self.p2.hand.cards) == 0 and len(self.p1.hand.cards) == 0:
            self.end_round()

        elif len(self.p1.hand.cards) == 0:
            self.handle_player_out_of_cards(self.p1, self.p2)

        elif len(self.p2.hand.cards) == 0:
            self.handle_player_out_of_cards(self.p2, self.p1)

        if not self.has_valid_card(self.p1) and not self.has_valid_card(self.p2):
            print("Neither play can play!")
            self.reset_table()

    def player_turn(self):
        self.check_go_list()

        if self.table_points == 31:
            print("31! + 1 point for computer. Resetting table points. (line 43)")
            self.p2_round_points += 1
            time.sleep(2)
            self.table_points = 0
            self.switch_turns()  

        print("-------------")
        print(f"{self.p1.name}'s turn!")
        self.display_hand(self.p1)
        
        
        if self.has_valid_card(self.p1):

            valid_input = False
            while not valid_input:
                input_index = self.get_valid_input(self.p1)

                if input_index is not None:  # Check if get_valid_input returns a valid index
                    chosen_card = self.p1.hand.cards[input_index]

                    if chosen_card.points + self.table_points <= 31:
                        valid_input = True
                        self.p1.hand.cards.pop(input_index) 
                        self.cards_played.append(chosen_card)
                        self.p1_cards_played.append(chosen_card)
                        self.table_points += chosen_card.points
                        print(f"{self.p1.name} plays {chosen_card}.")
                        print("-------------")
                        self.switch_turns()
                    else:
                        print("Invalid move. The selected card exceeds 31 points. Try again.")
                else:
                    print("Invalid input. Please enter a valid card position.")        

        else:
            self.go_list.append("Player 1 Go")
            print(f"{self.p1.name} cannot play. Go! + 1 point for Computer.")
            self.p2_round_points += 1
            print("-------------")
            input("Hit enter...")

    def computer_turn(self):
        self.check_go_list()

        if self.table_points == 31:
            print(f"31! + 1 point for {self.p1.name}. Resetting table points. (line 87)")
            self.p1_round_points += 1
            time.sleep(2)
            self.table_points = 0
            self.switch_turns()
        print(f"{self.p2.name}'s turn.")

        # Check if the computer has valid cards to play
        if self.has_valid_card(self.p2):
            valid_cards = [card for card in self.p2.hand.cards if card.points + self.table_points <= 31]
    
            if valid_cards:
                # If the computer has valid cards, it plays one randomly
                chosen_card = random.choice(valid_cards)
                self.p2.hand.cards.remove(chosen_card)
                self.p2_cards_played.append(chosen_card)
                self.cards_played.append(chosen_card)
                self.table_points += chosen_card.points

                print(f"{self.p2.name} plays {chosen_card}.")
            # Display the updated game state
            self.display_cards_played()
            print(f">> Table Points: {self.table_points}")

        else:
            # If the computer has no valid cards, it says "Go"
            self.go_list.append("Player 2 Go")
            print(f"Computer cannot play. Go! +1 point for {self.p1.name}.")
            self.p1_round_points += 1
            print("-------------")
            input("Hit enter...")

    def check_go_list(self):
        for _ in self.go_list:
            if "Player 1 Go" in self.go_list and "Player 2 Go" in self.go_list:
                print("Neither players can go.")
                input("Hit enter...")
                self.reset_table()
                self.go_list = []
            else:
                pass

    def switch_turns(self):
        if self.turn == self.p1:
            self.turn = self.p2
        elif self.turn == self.p2:
            self.turn = self.p1

    def handle_player_out_of_cards(self, player_out, other_player):
        print(f"{player_out.name} has run out of cards.")
        input("Hit enter...")

        while len(other_player.hand.cards) > 0:
            self.computer_turn() if player_out == self.p1 else self.player_turn()

            if not self.has_valid_card(other_player):
                if len(other_player.hand.cards) == 0 and len(player_out.hand.cards) == 0:
                    self.end_round()
                self.reset_table()
        
    def reset_table(self):
        print("Resetting table points to 0.")
        self.table_points = 0
        self.cards_played = []
        input("Hit enter...")

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
    
    def has_cards(self):
        return len(self.p1.hand.cards) > 0 and len(self.p2.hand.cards) > 0
    
    def has_valid_card(self, p):
        return any(card.points + self.table_points <= 31 for card in p.hand.cards)
    
    def end_round(self):
        input("Round over! Hit enter to calculate points...")
        time.sleep(2)
        self.p1_round_points += self.scoring.calc_points(self.p1_cards_played, self.p1)
        self.p2_round_points += self.scoring.calc_points(self.p2_cards_played, self.p2)
        print(f"Your score = {self.p1_round_points} | Computer score = {self.p2_round_points}")
        if self.p2_round_points == self.p1_round_points:
            print(f"It's a tie! Winner is...{random.choice([self.p1, self.p2])}")
        elif self.p1_round_points > self.p2_round_points:
            print("You win!")
        elif self.p2_round_points > self.p1_round_points:
            print("Computer wins.")
        sys.exit()

    def display_hand(self, p):
        print(f"{p.name}'s Hand: {', '.join(str(card) for card in p.hand.cards)}")

    def display_cards_played(self):
        print(f">> Cards Played: {', '.join(str(card) for card in self.cards_played)}")



