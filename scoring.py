import itertools

class Scoring:
    '''
    Cribbage Scoring:
    - Calculates points based on specific combinations of cards in the game of cribbage.
    - Supports scoring for 15s and pairs.
    '''

    def __init__(self):
        pass

    def calc_points(self, card_list, player):
        print(f"{player.name}'s hand: " + ", ".join(str(card) for card in card_list))
        points = 0
    
        # Check for any combination of cards that equal 15
        for subset_size in range(1, len(card_list) + 1):
            for subset in itertools.combinations(card_list, subset_size):
                if sum(card.points for card in subset) == 15:
                    points += 2

        # Check for any two cards that are the same value
        for i in range(len(card_list)):
            for j in range(i + 1, len(card_list)):
                if card_list[i].value == card_list[j].value:
                    points += 2
        
        return points 

