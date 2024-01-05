from card import Card
from termcolor import colored
import random

class Deck:
    '''
    Represents a deck of cards with methods for generating, shuffling, and dealing cards.
    '''

    def __init__(self):
        self.values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.suits = [colored("♣", 'black'), colored("♥", 'red'), colored("♠", 'black'), colored("♦", 'red')]
        self.cards = self.generate_deck()

    def __str__(self):
        return '\n'.join(map(str, self.cards))

    def generate_deck(self):
        deck = []
        for value in self.values:
            for suit in self.suits:
                if value == "A":
                    points = 1
                elif value in ["J", "Q", "K"]:
                    points = 10
                else:
                    points = value
                card = Card(value, suit, points)
                deck.append(card)
        return deck

    def deal(self, players):
        '''
        Deal cards to players from the deck.
        - Args: List of player objects to whom cards are dealt.
        '''
        for _ in range(6): 
            for player in players:
                card = self.cards.pop(0) 
                player.hand.add_card(card)

    def shuffle(self):
        random.shuffle(self.cards)

