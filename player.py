from hand import Hand

class Player:
    def __init__(self, name):
        self._name = name
        self.hand = Hand()

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return self._name
    
    @classmethod
    def create_player(cls):
        while True:
            name = input("Enter player's name: ")
            if len(name) >= 1:
                return cls(name)
            else:
                print("Invalid input. Please enter a name with at least one character.")