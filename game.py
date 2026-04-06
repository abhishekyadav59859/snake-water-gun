import random
import datetime

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    wins = {
        "snake": "water",
        "water": "gun",
        "gun": "snake"
    }
    if wins[player] == computer:
        return "player"
    return "computer"

def get_best_score():
    try:
        with open("score_history.txt", "r") as f:
            lines = f.readlines()
        best = 0
        for line in lines:
            if "You:" in line:
                score = int(line.split("You:")[1].split("|")[0].strip())
                if score > best:
                    best = score
        return best
    except FileNotFoundError:
        return 0

def save_score(player_score, computer_score, rounds):
    prev_best = get_best_score()
    with open("score_history.txt", "a") as f:
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        f.write(f"Date: {now} | Rounds: {rounds} | You: {player_score} | Computer: {computer_score}\n")
    print("\nScore saved to score_history.txt!")
    if player_score > prev_best:
        print("🏆 New Personal Best! You scored", player_score, "wins!")
    else:
        print(f" Your best score so far: {prev_best} wins — keep going!")

def show_history():
    try:
        with open("score_history.txt", "r") as f:
            history = f.readlines()
        if not history:
            print("No history found yet.")
        else:
            print("\n--- Score History ---")
            for line in history:
                print(line.strip())
            print("---------------------")
            best = get_best_score()
            print(f" Your All-Time Best: {best} wins in a single game")
            print("---------------------")
    except FileNotFoundError:
        print("No history found yet. Play a game first!")

def play_game():
    print("=" * 40)
    print("   Welcome to Snake, Water, Gun!")
    print("=" * 40)

    best = get_best_score()
    if best > 0:
        print(f" Your current best: {best} wins")

    print("\n1. Play game")
    print("2. View score history")
    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "2":
        show_history()
        return

    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\nChoose: snake / water / gun  (or 'quit' to exit)")
        player = input("Your choice: ").strip().lower()

        if player == "quit":
            break

        if player not in ["snake", "water", "gun"]:
            print("Invalid choice. Please type snake, water, or gun.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        result = determine_winner(player, computer)
        rounds += 1

        if result == "player":
            player_score += 1
            print(" You win this round!")
        elif result == "computer":
            computer_score += 1
            print(" Computer wins this round!")
        else:
            print(" It's a draw!")

        print(f"Score — You: {player_score} | Computer: {computer_score}")

    print("\n" + "=" * 40)
    print(f"Game over! Rounds played: {rounds}")
    print(f"Final Score — You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print(" You won the game! Well played.")
    elif computer_score > player_score:
        print(" Computer won the game. Better luck next time!")
    else:
        print(" It's a tie overall!")
    print("=" * 40)

    if rounds > 0:
        save_score(player_score, computer_score, rounds)

if __name__ == "__main__":
    play_game()