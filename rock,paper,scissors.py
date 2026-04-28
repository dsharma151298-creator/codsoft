import random

print("\nROCK PAPER SCISSORS GAME")
print("Instructions:")
print("Enter rock, paper or scissors to play.")
print("Type quit anytime to exit.")

opts = ("rock", "paper", "scissors")
alt_opts = ("scissors", "rock", "paper")

player_score = 0
cpu_score = 0

while True:

    user_input = input("\nChoose (rock/paper/scissors): ").lower()
    cpu_choice = random.choice(opts)

    if user_input == "quit":
        print("\nGame over!")
        break

    if user_input not in opts:
        user_input = input("Please enter a valid option: ").lower()

    print(f"\nYou chose: {user_input}")
    print(f"CPU chose: {cpu_choice}")

    if user_input == cpu_choice:
        print("Tie!")

    elif opts.index(user_input) == alt_opts.index(cpu_choice):
        print("You win!")
        player_score += 1

    else:
        print("You lose!")
        cpu_score += 1

    replay = input("\nPlay again? (y/n): ").lower()
    if replay != "y":
        break


print("\nScoreboard:")
print("Player:", player_score)
print("CPU:", cpu_score)
print("Thanks for playing!\n")