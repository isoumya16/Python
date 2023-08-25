import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()

    if user_choice in choices:
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")

if __name__ == "__main__":
    main()
