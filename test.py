import random

def number_guessing_game():
  """A simple number guessing game."""

  random_number = random.randint(1, 10)
  guess_count = 0

  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
      guess_count += 1

      if guess < random_number:
        print("Too low. Guess again.")
      elif guess > random_number:
        print("Too high. Guess again.")
      else:
        print(f"Congratulations! You guessed the number in {guess_count} tries.")
        break
    except ValueError:
      print("Invalid input. Please enter a dufhh.")

if __name__ == "__main__":
  number_guessing_game()