# Snake, Water, Gun Game

A Python command-line game based on the classic Indian hand game —
Snake, Water, Gun. Similar to Rock, Paper, Scissors.

## Rules

- Snake drinks Water — Snake wins
- Water drowns Gun — Water wins
- Gun kills Snake — Gun wins
- Same choice — Draw

## How to play
```bash
python game.py
```

Type `snake`, `water`, or `gun` when prompted.
Type `quit` to exit the game.

## Features

- Play unlimited rounds against the computer
- Real-time score tracking
- Input validation — handles wrong inputs gracefully
- Clean game summary at the end
- Score history — saves every game result with date and time to score_history.txt
- View past scores from the main menu

## What I learned building this

- Python functions and modular code structure
- Random module for computer AI
- User input handling and validation
- Score tracking and game loop logic
- File handling — reading and writing to text files
- datetime module for timestamping records
- Git workflow — commits, push, pull, merge

## Tech used

Python 3 — no external libraries required