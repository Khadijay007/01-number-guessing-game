import random


def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n=================================")
    print("       NUMBER GUESSING GAME")
    print("=================================")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < number:
                print("Too Low! Try again.")

            elif guess > number:
                print("Too High! Try again.")

            else:
                print("\n🎉 Correct!")
                print(f"You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        play_game()

        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
