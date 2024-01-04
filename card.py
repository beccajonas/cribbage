class Card:
    def __init__(self, value, suit, points):
        self.value = value
        self.suit = suit
        self.points = points

    def __str__(self) -> str:
        return f"{self.value} {self.suit}"