import random

def RPS() -> None:
    user_score = 0
    computer_score = 0

    while True:
        x = input("Rock, paper, or scissor? Go!: ")
        y = random.randint(1, 3)

        if y == 1:
            computer = "rock"
        elif y == 2:
            computer = "paper"
        else:
            computer = "scissor"

        print(f"Computer chose: {computer}")

        if x.lower() == "rock" and computer == "rock":
            print("tie")
        elif x.lower() == "rock" and computer == "paper":
            print("You lose")
            computer_score += 1
        elif x.lower() == "rock" and computer == "scissor":
            print("You win")
            user_score += 1
        elif x.lower() == "paper" and computer == "rock":
            print("You win")
            user_score += 1
        elif x.lower() == "paper" and computer == "paper":
            print("tie")
        elif x.lower() == "paper" and computer == "scissor":
            print("You lose")
            computer_score += 1
        elif x.lower() == "scissor" and computer == "rock":
            print("You lose")
            computer_score += 1
        elif x.lower() == "scissor" and computer == "paper":
            print("You win")
            user_score += 1
        elif x.lower() == "scissor" and computer == "scissor":
            print("tie")
        else:
            print("Invalid input")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    # Display the final score and end the game
    print(f"Final score: user: {user_score} | computer: {computer_score}")

RPS()
