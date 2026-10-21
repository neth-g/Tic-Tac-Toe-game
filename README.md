# Python Tic-Tac-Toe: From Random Bots to Unbeatable Minimax Algorithm

A progressive Python implementation of Tic-Tac-Toe through four levels of bot difficulty, ranging from completely random moves to an unbeatable algorithm.

## Game Levels & AI Breakdown

This repository contains four .py files, each showcasing a different level of logic, algorithms, and decision-making for the opponent:

**Level 1: Random Bot (TicTacToe-lvl1.py)**
Bot chooses available moves completely at random without any strategic logic or evaluation.
Difficulty: Very Easy.

**Level 2: One-Step Lookahead Bot (TicTacToe-lvl2.py)**
Bot checks one turn ahead. It will actively take a winning move if available or block you if you are about to win on the next turn. Otherwise, it makes a default/random move.
Difficulty: Easy.

**Level 3: Win-Probability Bot (TicTacToe-lvl3.py)**
Bot evaluates the current board state and simulates all possible outcomes to select the move with the highest statistically calculated chance of victory.
Difficulty: Medium / Hard.

**Level 3.5: Minimax Bot — Unbeatable (ticTacToe-lvl3.5.py)**
Implements the Minimax Algorithm, exploring every possible move tree down to terminal states. It maximizes its own chances of winning while assuming optimal play from the opponent.
Difficulty: Unbeatable.

## How to Run

1. Clone or Download the Repository
2. Run any version using Python 3
3. Try to beat the bot!

## Concepts & Technologies Used
Language: Python 3
Concepts: Game loops & command-line interface design, State evaluation & conditional branching, Rcursive search algorithms, Probability-based evaluations
