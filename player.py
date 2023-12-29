from hand import Hand

class Player:
    def __init__(self, name):
        self._name = name
        self.hand = Hand()
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) < 1:
            raise ValueError("Please enter a name with at least one character")
        self._name = name

    

