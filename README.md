# 🐍 Snake, Water, Gun Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-CLI-black?style=for-the-badge&logo=windowsterminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

> **A Python command-line game based on the classic Indian hand game — Snake, Water, Gun.**
> Similar to Rock, Paper, Scissors but with a desi twist! 🇮🇳

</div>

---

## 🎮 Game Rules

```
        🐍 SNAKE
       /        \
      /          \
drinks           killed by
     \            /
      \          /
    💧 WATER --drowns--> 🔫 GUN
```

| Player    | Beats    | Loses To  |
|-----------|----------|-----------|
| 🐍 Snake  | 💧 Water  | 🔫 Gun    |
| 💧 Water  | 🔫 Gun    | 🐍 Snake  |
| 🔫 Gun    | 🐍 Snake  | 💧 Water  |
| Same choice | —      | Draw 🤝   |

---

## 📂 Project Structure

```
snake-water-gun/
│
├── game.py              # Main game logic
├── score_history.txt    # Auto-generated after first game
└── README.md            # You are here!
```

---

## ▶️ How to Play

### 1. Clone the repo
```bash
git clone https://github.com/abhishekyadav59859/snake-water-gun.git
cd snake-water-gun
```

### 2. Run the game
```bash
python game.py
```

### 3. Follow the prompts

```
========================================
   Welcome to Snake, Water, Gun!
========================================
🏆 Your current best: 4 wins

1. Play game
2. View score history

Enter 1 or 2: 1

Choose: snake / water / gun  (or 'quit' to exit)
Your choice: snake
Computer chose: water
✅ You win this round!
Score — You: 1 | Computer: 0

...

========================================
Game over! Rounds played: 5
Final Score — You: 5 | Computer: 0
🎉 You won the game! Well played.
========================================
Score saved to score_history.txt!
🏆 New Personal Best! You scored 5 wins!
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🎮 Unlimited Rounds | Play as many rounds as you want |
| 🤖 Computer AI | Random computer moves every round |
| 📊 Live Score | Real-time score shown after every round |
| ✅ Input Validation | Handles typos and wrong inputs gracefully |
| 🏆 Personal Best Tracker | Tracks and celebrates your all-time highest score |
| 💾 Score History | Saves every game result to `score_history.txt` |
| 📅 Timestamps | Every saved game includes date and time |
| 📜 View History | Check past game scores from the main menu |

---

## 🔄 Game Flow

```
         START
           │
           ▼
    ┌─────────────┐
    │  Main Menu  │◄── Shows your current best score
    └──────┬──────┘
           │
     ┌─────┴──────┐
     │            │
     ▼            ▼
  Play Game   View History
     │              │
     │         Shows all-time best
     ▼
 Enter Choice
 (snake/water/gun)
     │
     ▼
 Computer picks
 random choice
     │
     ▼
 Determine Winner
 ┌───┴────┐────┐
 ▼        ▼    ▼
Win ✅  Lose ❌  Draw 🤝
     │
     ▼
 Continue or Quit?
     │
     ▼
 Save Score → Check Personal Best
     │
     ▼
   END
```

---

## 🧠 What I Learned Building This

- 🔧 Python functions and modular code structure
- 🎲 `random` module for computer AI
- 🖊️ User input handling and validation
- 📈 Score tracking and game loop logic
- 📁 File handling — reading & writing to text files
- ⏰ `datetime` module for timestamping records
- 🏆 Parsing saved data to compute personal best scores
- 🌿 Git workflow — commits, push, pull, merge

---

## 🛠️ Tech Used

```
Language  : Python 3
Libraries : random, datetime (built-in — no installs needed!)
Platform  : Command Line Interface (CLI)
```

---

## 🚀 Future Plans

- [ ] Add difficulty levels (easy / hard computer AI)
- [ ] Add multiplayer (2 players on same machine)
- [ ] Add a best-of-3 or best-of-5 mode
- [ ] Convert to GUI using Tkinter
- [ ] Add a leaderboard system
- [ ] Add colorful output using colorama library
- [ ] Add a High Score display in terminal
- [ ] Add a difficulty mode — Easy / Medium / Hard

---

## 👤 Author

**Abhishek Yadav**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/abhishekyadav59859)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github&logoColor=white)](https://github.com/abhishekyadav59859)
[![Gmail](https://img.shields.io/badge/Gmail-Mail-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:abhishekyadav59859@gmail.com)

---

<div align="center">
  Made with ❤️ and Python 🐍
  <br/>
  ⭐ Star this repo if you liked it!
</div>