from hand import Hand

class Player:
    def __init__(self, is_dealer, name):
        self._name = name
        self.hand = Hand()
        self._is_dealer = is_dealer

    @property
    def is_dealer(self):
        return self._is_dealer
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) < 1:
            raise ValueError("Please enter a name with at least one character")
        self._name = name

    @property
    def dealer_status(self):
        return "Dealer" if self.is_dealer else "Not Dealer"
    

