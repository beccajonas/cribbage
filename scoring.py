import itertools

class Scoring:
    '''
    Cribbage Scoring:
    - Calculates points based on specific combinations of cards in the game of cribbage.
    - Supports scoring for 15s and pairs.
    '''

    def __init__(self):
        self.values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def calc_points(self, card_list):
        print(", ".join(str(card) for card in card_list))
        points = 0
    
        # Check for any combination of cards that equal 15
        for subset_size in range(1, len(card_list) + 1):
            for subset in itertools.combinations(card_list, subset_size):
                if sum(self.get_numeric_value(card) for card in subset) == 15:
                    points += 2

        # Check for any two cards that are the same value
        for i in range(len(card_list)):
            for j in range(i + 1, len(card_list)):
                if card_list[i].value == card_list[j].value:
                    points += 2
        
        return points 
    
    def get_numeric_value(self, card):
        if card.value == "A":
            return 1
        elif card.value in ["J", "Q", "K"]:
            return 10
        else:
            return int(card.value)



        

