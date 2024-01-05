import time
import sys
from termcolor import colored

class Animations:
    def __init__(self):
        self.shuffle = [
            colored('♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥', 'red'), 
            colored('♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠', 'black'), 
            colored('♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦', 'red'),
            colored('♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣', 'black')]
        
        self.calculating = [
            colored('+ + + + + + + + +', 'green'),
            colored('= = = = = = = = =', 'blue'),
            colored('+ + + + + + + + +', 'green'),
            colored('= = = = = = = = =', 'blue')
        ]
        

    def display_shuffle(self):
        for i in range(10):
          time.sleep(0.2)
          sys.stdout.write("\r" + self.shuffle[i % len(self.shuffle)])
          sys.stdout.flush()

    def display_calculating(self):
        for i in range(15):
            time.sleep(0.2)
            sys.stdout.write("\r" + self.calculating[i % len(self.calculating)])
            sys.stdout.flush()
          
    def display_winner(self):
        colors = ["red", "white", "green", "blue"]
        for i in range(3):
            for color in colors:
                time.sleep(0.2)
                sys.stdout.write("\r" + colored("♠ ♠ ♠ YOU WIN! ♠ ♠ ♠\n♥ ♥ ♥ YOU WIN! ♥ ♥ ♥ \n♣ ♣ ♣ YOU WIN! ♣ ♣ ♣\n♦ ♦ ♦ YOU WIN! ♦ ♦ ♦ ", color, attrs=['bold']))
                sys.stdout.flush()
    
    def display_loser(self):
        colors = ["red", "white", "green", "blue"]
        thumbs_down = "\U0001F44E"
        for i in range(3):
            for color in colors:
                time.sleep(0.2)
                message = f"{thumbs_down} YOU LOSE! {thumbs_down}"
                formatted_message = colored(message, color, attrs=['bold'])
                sys.stdout.write("\r" + formatted_message + '\n')
                sys.stdout.flush()