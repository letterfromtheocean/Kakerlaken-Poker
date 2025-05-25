# Kakerlaken-Poker

A Python implementation of the classic bluffing card game **Kakerlaken Poker** (Cockroach Poker), playable in the terminal for 2-6 players.

## Game Introduction
Kakerlaken Poker is a fun bluffing game where players try to avoid collecting four cards of the same animal. Each turn, a player passes a card face down to another player and claims it is a certain animal (truthfully or not). The receiving player must decide whether to believe the claim, doubt it, or pass the card on. The game is all about bluffing, deduction, and reading your opponents!

## Rules
- There are 8 types of animals, each with 8 cards (total 64 cards):
  - Cockroach, Bat, Fly, Toad, Rat, Scorpion, Spider, Stinkbug
- Cards are shuffled and dealt evenly to all players.
- On your turn:
  1. Choose a card from your hand.
  2. Choose a player to pass it to.
  3. Declare an animal (truth or lie).
- The receiving player can:
  - **Believe**: If the claim is true, the passing player takes the card face up. If false, the receiver takes it face up.
  - **Doubt**: If the claim is false, the passing player takes the card face up. If true, the receiver takes it face up.
  - **Pass**: Look at the card and pass it to another player (not the previous one), making a new claim. The next player must then believe or doubt.
- The card is always revealed and placed face up in front of the appropriate player after the challenge.
- If a player has no cards in hand, they are skipped on their turn.
- **Game ends** when a player has 4 cards of the same animal face up in front of them (that player loses), or when all cards are played (the player with the most of a single animal loses).

## How to Run
1. Make sure you have Python 3 installed.
2. Download `Kakerlaken_Poker.py` to your computer.
3. Open a terminal and navigate to the script's directory.
4. Run:
   ```bash
   python3 Kakerlaken_Poker.py
   ```

## Game Controls & Input
- Enter the number of players (2-6) and each player's name.
- On your turn, follow the prompts to select a target, choose a card, and declare an animal.
- Input is case-insensitive for animal names.
- When receiving a card, choose to believe, doubt, or pass (only once per card).

## Animal List
- Cockroach
- Bat
- Fly
- Toad
- Rat
- Scorpion
- Spider
- Stinkbug
