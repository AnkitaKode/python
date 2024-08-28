import random

def rock_paper_scissors():
    print("Welcome to 'Rock, Paper, Scissors' Game!")
    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors()
