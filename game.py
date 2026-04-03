import random

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

def play_game():
    print("=" * 40)
    print("   Welcome to Snake, Water, Gun!")
    print("=" * 40)

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
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score — You: {player_score} | Computer: {computer_score}")

    print("\n" + "=" * 40)
    print(f"Game over! Rounds played: {rounds}")
    print(f"Final Score — You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("You won the game! Well played.")
    elif computer_score > player_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("It's a tie overall!")
    print("=" * 40)

if __name__ == "__main__":
    play_game()