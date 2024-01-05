# Cribbage Game

## Introduction
Welcome to the Cribbage! This Python program allows you to play Cribbage against a computer opponent. Cribbage is a classic card game that involves creating combinations of cards to score points.

<img width="821" alt="Welcome to Cribbage" src="https://github.com/beccajonas/cribbage/assets/87732074/a812309f-4ce6-4285-9cac-74c169e78102">

## Getting Started
To start the game, run the `main.py` file. The game will begin by shuffling the deck, dealing cards to you and the computer player, and filling the crib.

## Game Components
### Classes
1. **Main Class (`main.py`):**
   - Responsible for initializing the game components.
   - Manages the main flow of the game.

2. **Round Class (`round.py`):**
   - Controls the logic for each round of the game.
   - Handles player and computer turns, scoring, and round end.

3. **Scoring Class (`scoring.py`):**
   - Calculates points based on specific card combinations in the game.

4. **Crib Class (`crib.py`):**
   - Manages the initial game setup for establishing the crib.

5. **Hand Class (`player.py`):**
   - Represents a player's hand and provides methods for adding, discarding, and displaying cards.

6. **Card Class (`player.py`):**
   - Represents a playing card with a value, suit, and point value.

### Functions
1. **Main Class Functions:**
   - `fill_crib()`: Shuffles and deals cards, allowing players to discard cards to fill the crib.

2. **Round Class Functions:**
   - `play()`: Manages the flow of a round, alternating between player and computer turns.
   - `player_turn()`: Handles the player's turn.
   - `computer_turn()`: Manages the computer's turn.
   - `switch_turns()`: Switches turns between player and computer.
   - `handle_player_out_of_cards()`: Manages the end of the round if a player runs out of cards.
   - `reset_table()`: Resets the table points and cards played.
   - `end_round()`: Calculates and displays points at the end of a round.

3. **Scoring Class Functions:**
   - `calc_points(card_list, player)`: Calculates points based on card combinations.
   
<img width="683" alt="31 scoring" src="https://github.com/beccajonas/cribbage/assets/87732074/c0dcf209-24a0-4f64-8568-c2b7eb7284c7">

4. **Crib Class Functions:**
   - `discard(p)`: Allows the player to discard cards to the crib.
   - `computer_discard(p)`: Allows the computer to discard cards to the crib.

## Unit Testing
`test_scoring.py`: Ensures the correctness of the scoring functionality with unit tests.

## How to Play
1. Follow the on-screen instructions to fill the crib with discarded cards.
2. The game will alternate between your turn and the computer's turn.
3. During your turn, choose a card to play by entering the corresponding card number.
4. The computer will then take its turn.
5. The round continues until both players cannot play or run out of cards, keeping score when the table count of "31" is hit by a player.
6. Points are calculated based on card combinations at the end of each round. This version currently supports scoring for pairs and combinations that equal 15.
7. The game ends when a player reaches the maximum score or when you decide to exit.
   
<img width="691" alt="Final scoring" src="https://github.com/beccajonas/cribbage/assets/87732074/831d8385-5570-46df-8a31-2624e62ea186">

Enjoy playing Cribbage!
