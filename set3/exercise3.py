"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def super_asker(low, high, message):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """

    while True:
        my_input = int(input(message))
        try:
            val = int(my_input)
            if low <= my_input <= high:
                return my_input
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("incorrect try again:")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    low = super_asker(-5000, 5000, "Enter a lower bound: ")
    high = super_asker(low, 5000, "Enter an upper bound: ")
    print(f"OK then, guess a number between {low} and {high} ?")
    actualNumber = random.randint(low, high)

    attempts = 0
    while True:
        guess = super_asker(low, high, "Enter your guess: ")
        attempts += 1

        if guess < actualNumber:
            print("Too low! Try again.")
        elif guess > actualNumber:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
