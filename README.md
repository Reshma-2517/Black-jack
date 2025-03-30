# Black-jack
This Python program simulates a Blackjack game, allowing players to compete against a dealer. It includes card dealing, hit/stand options, and hand evaluation based on standard Blackjack rules.

Description:
This is a simple text-based Blackjack game implemented in Python. The player competes against the computer, drawing cards to get as close to 21 as possible without exceeding it. The game allows the player to hit or stand, while the computer follows predefined rules.

Features:
Random card selection using the random module
Player can hit (draw more cards) or stand
Computer also plays by drawing cards until it reaches a minimum threshold
Automatic win/loss detection (Bust, Win, Push)

How to Play
Run the Python script:
python blackjack.py
The game will randomly assign two cards to the player and one to the computer.
The player can choose to "hit" (draw another card) or "stand" (keep their current total).
The computer will then draw cards until it reaches at least 18.
The winner is decided based on who gets closer to 21 without going over.

Requirements:
Python 3.x
