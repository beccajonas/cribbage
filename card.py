from termcolor import colored

class Card:
    def __init__(self, value, suit, points):
        self.value = value
        self.suit = suit
        self.points = points

    def __str__(self):
        suit_color = 'white' 
        value_color = 'white'
        if self.suit == colored("♥", 'red') or self.suit == colored("♦", 'red'):
            suit_color = 'red'

        if value_color == 'white':
            value_color = 'red' if suit_color == 'red' else 'black'

        return f"{colored(self.value, value_color)} {colored(self.suit, suit_color)}"   
    