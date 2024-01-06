import itertools

class Scoring:
    '''
    Cribbage Scoring:
    - Calculates points based on specific combinations of cards in the game of cribbage.
    - Supports scoring for 15s, pairs and 3-card runs in hand.
    '''

    def __init__(self):
        pass

    def calc_points(self, card_list, player):
        print(f"{player.name}'s hand: " + ", ".join(str(card) for card in card_list))
        points = 0
    
        # Check for any combination of cards that equal 15
        for subset_size in range(1, len(card_list) + 1):
            for subset in itertools.combinations(card_list, subset_size):
                subset_expression = " + ".join(f"{card.value} {card.suit}" for card in subset)
                
                if sum(card.points for card in subset) == 15:
                    print(f"{subset_expression} = 15")
                    points += 2

        # Check for any two cards that are the same value
        for card1, card2 in itertools.combinations(card_list, 2):
            if card1.value == card2.value:
                print(f"{card1} and {card2} are pairs.")
                points += 2

        # Check for 3 card run 
        allowed_values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        for three_card_combo in itertools.permutations(card_list, 3):
            values = [card.value for card in three_card_combo]
            indices = [allowed_values.index(value) for value in values]

            if all(indices[i] == indices[i + 1] - 1 for i in range(len(indices) - 1)):
                print(f"{' '.join(str(card) for card in three_card_combo)} for a run")
                points += 3

        return points 


