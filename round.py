from animations import Animations
from termcolor import colored
from scoring import Scoring
import random
import sys
import os

class Round:
    def __init__(self, p1, p2):
        self.p1 = p1 
        self.p2 = p2 # Computer player
        self.turn = random.choice([p1, p2])
        self.p1_cards_played = []
        self.p1_round_points = 0
        self.p2_cards_played = []
        self.p2_round_points = 0
        self.cards_played = [] # Combination of both players cards played
        self.table_points = 0 
        self.go_list = [] # Frequency of "Player 1 Go" or frequency of "Player 2 Go" cannot exceed 1. 
        self.scoring = Scoring()
        self.animations = Animations()
        
    def play(self):
        while self.has_cards():
            if self.turn == self.p1:
                self.player_turn()
                self.computer_turn()
                self.switch_turns()
            else:
                self.computer_turn()
                self.player_turn()
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
            print(colored(f"31! + 1 point for Computer.", "green", attrs=['bold']))
            self.p2_round_points += 1
            self.table_points = 0
            self.switch_turns()  
            input("-------------")
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
                        print(colored("Invalid move. The selected card exceeds 31 points. Try again.", 'red'))
                else:
                    print(colored("Invalid input. Please enter a valid card position.", "red"))        

        else:
            self.go_list.append("Player 1 Go")
            print(f"{self.p1.name} cannot play. Go!")
            input("-------------")

    def computer_turn(self):
        self.check_go_list()

        if self.table_points == 31:
            print(colored(f"31! + 1 point for {self.p1.name}.", "green", attrs=['bold']))
            self.p1_round_points += 1
            self.table_points = 0
            self.switch_turns()
            input("-------------")
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
            print(colored(f">> Table Points: {self.table_points}", "blue"))
            input("-------------")

        else:
            # If the computer has no valid cards, it says "Go"
            self.go_list.append("Player 2 Go")
            print(f"Computer cannot play. Go!")
            input("-------------")

    def check_go_list(self):
        for _ in self.go_list:
            if "Player 1 Go" in self.go_list and "Player 2 Go" in self.go_list:
                print("Neither players can go.")
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

        while len(other_player.hand.cards) > 0:
            self.computer_turn() if player_out == self.p1 else self.player_turn()

            if not self.has_valid_card(other_player):
                if len(other_player.hand.cards) == 0 and len(player_out.hand.cards) == 0:
                    self.end_round()
                self.reset_table()
        
    def reset_table(self):
        print("Resetting table points to 0.")
        input("Hit enter to clear screen.")
        self.table_points = 0
        self.cards_played = []
        os.system('clear')

    def get_valid_input(self, p):
        while True:
            input_index_string = input("Select the number of a card you want to play >> ")
            if input_index_string.isdigit():
                input_index = int(input_index_string) - 1
                if input_index in range(0, len(p.hand.cards)):
                    return input_index
                else:
                    print(colored("Invalid input. Please enter a valid card position.", "red"))
            else: print(colored("Invalid input. Please enter a valid card position.", "red"))
    
    def has_cards(self):
        return len(self.p1.hand.cards) > 0 and len(self.p2.hand.cards) > 0
    
    def has_valid_card(self, p):
        return any(card.points + self.table_points <= 31 for card in p.hand.cards)
    
    def end_round(self):
        input("Round over! Hit enter to calculate points...")
        self.animations.display_calculating()
        print()
        self.p1_round_points += self.scoring.calc_points(self.p1_cards_played, self.p1)
        self.p2_round_points += self.scoring.calc_points(self.p2_cards_played, self.p2)
        print(colored(f"{self.p1.name}'s score = {self.p1_round_points} | Computer score = {self.p2_round_points}", "green"))
        if self.p2_round_points == self.p1_round_points:
            winner = random.choice([self.p1, self.p2])
            print(f"It's a tie! Winner is... {winner}!")
            if winner == self.p1:
                input("You win! Hit enter to celebrate!")
                os.system('clear')
                self.animations.display_winner()
            else:
                input("You lose! Hit enter to wallow in self pity.")
                os.system('clear')
                self.animations.display_loser()
        elif self.p1_round_points > self.p2_round_points:
            input("You win! Hit enter to celebrate!")
            os.system('clear')
            self.animations.display_winner()
        else:
            input("You lose! Hit enter to wallow in self pity.")
            os.system('clear')
            self.animations.display_loser()
        sys.exit()

    def display_hand(self, p):
        print(f"{p.name}'s Hand: {', '.join(str(card) for card in p.hand.cards)}")

    def display_cards_played(self):
        print(f">> Cards Played: {', '.join(str(card) for card in self.cards_played)}")



