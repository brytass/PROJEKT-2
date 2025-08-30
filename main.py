"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Radek Marval
email: marvalradek@seznam.cz
"""

import random
import time
from typing import List, Tuple


separator = "-----------------------------------------------"


def welcome() -> None:
    """
    Print a welcome message and rules for the Bulls and Cows game.
    """
    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)



def generate_unique_4digit_number() -> List[int]:
    """
    Generate a random 4-digit number with unique digits.

    Returns:
        List[int]: A list of 4 unique integers representing the digits.
    """
    while True:
        number: int = random.randint(1000, 9999)
        digits: str = str(number)
        if len(set(digits)) == 4:
            return [int(d) for d in digits]



def is_valid_input(user_input: str) -> bool:
    """
    Validate the user's input for the Bulls and Cows game.
    """
    if not user_input.isdigit():
        print("Please use only digits.")
        return False
    if len(user_input) != 4:
        print("Please enter exactly 4 digits.")
        return False
    if user_input[0] == "0":
        print("Number must not start with 0.")
        return False
    if len(set(user_input)) != 4:
        print("Digits must be unique.")
        return False
    return True



def bulls_and_cows(secret: List[int], guess: List[int]) -> Tuple[int, int]:
    """
    Compare the secret number with the user's guess and calculate
    the number of bulls and cows.

    Args:
        secret (List[int]): The secret 4-digit number as a list of digits.
        guess (List[int]): The guessed 4-digit number as a list of digits.

    Returns:
        Tuple[int, int]: (bulls, cows)
    """

    # "bull" = správná číslice na správné pozici
    # zip spojí dvojice číslic ze secret a guess → [(s1, g1), (s2, g2), ...]
    # pak jednoduše sečteme, kolikrát jsou stejné
    bulls = sum(s == g for s, g in zip(secret, guess))

    # "cow" = číslice existuje v obou číslech, ale není na správné pozici
    # vezmeme všechny unikátní číslice z guess (set(guess))
    # pro každou spočítáme, kolikrát se vyskytuje v obou číslech
    # → to nám dá i bulls + cows
    # na konci odečteme bulls, aby zůstaly jenom cows
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls

    return bulls, cows



def print_result(bulls: int, cows: int) -> None:
    """
    Print the result of the current guess in a human-readable format.
    """
    bull_word: str = "bull" if bulls == 1 else "bulls"
    cow_word: str = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
    print(separator)



def main() -> None:
    """
    Main function to run the Bulls and Cows game.
    """
    welcome()
    secret_number: List[int] = generate_unique_4digit_number()
    attempts: int = 0
    start_time: float = time.time()

    while True:
        user_input: str = input(
            "Enter a number:\n-----------------------------------------------\n"
        ).strip()

        if not is_valid_input(user_input):
            continue

        guess: List[int] = [int(d) for d in user_input]
        attempts += 1
        bulls, cows = bulls_and_cows(secret_number, guess)

        if bulls == 4:
            elapsed_time: float = time.time() - start_time
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print("That's amazing!")
            print(f"It took you {elapsed_time:.2f} seconds.")
            break
        else:
            print_result(bulls, cows)



if __name__ == "__main__":
    main()
