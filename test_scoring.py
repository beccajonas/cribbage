import pytest
from scoring import Scoring
from card import Card 
from player import Player

class TestScoring:
    def test_calc_points_15_two_combinations(self):
        card_list = [Card(5, "♥", 5), Card(10, "♦", 10), Card("A", "♦", 1), Card(4, "♠", 4)]
        player = Player("Player")
        scoring = Scoring()
        result = scoring.calc_points(card_list, player)
        assert result == 4, f"Expected result: 4, Actual result: {result} | 5 ♥ + 10 ♦ = 15 and A ♦ + 4 ♠ = 15"

    def test_calc_points_pair_and_three_card_15(self):
        card_list = [Card(3, "♥", 3), Card(9, "♦", 9), Card(3, "♦", 3), Card(4, "♠", 4)]
        player = Player("Player")
        scoring = Scoring()
        result = scoring.calc_points(card_list, player)
        assert result == 4, f"Expected result: 4, Actual result: {result} | 3 ♥ + 9 ♦ + 3 ♦ = 15, 3 ♦ and 3 ♥ is a pair"

    def test_calc_points_many_pairs(self):
        card_list = [Card(2, "♥", 2), Card(2, "♦", 2), Card(10, "♣", 10), Card(2, "♠", 2)]
        player = Player("Player")
        scoring = Scoring()
        result = scoring.calc_points(card_list, player)
        assert result == 6, f"Expected result: 6, Actual result: {result} | 2 ♥ + 2 ♦ = pair, 2 ♥ + 2 ♠ = pair, 2 ♦ + 2 ♠ = pair"

    def test_calc_0_points(self):
        card_list = [Card(2, "♥", 2), Card("A", "♦", 1), Card(8, "♣", 8), Card("K", "♠", 10)]
        player = Player("Player")
        scoring = Scoring()
        result = scoring.calc_points(card_list, player)
        assert result == 0, f"Expected result: 0, Actual result: {result} | No pairs or combinations that equal 15."

    def test_3_card_run(self):
        card_list = [Card(2, "♥", 2), Card("A", "♦", 1), Card(3, "♣", 3), Card("K", "♠", 10)]
        player = Player("Player")
        scoring = Scoring()
        result = scoring.calc_points(card_list, player)
        assert result == 5, f"Expected result: 5, Actual result: {result} | ('A' ♦, 2 ♥, 3 ♣) for 3 points, 2 ♥ + 3 ♣ + 10 ♠ = 15."