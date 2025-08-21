"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Radek Marval
email: marvalradek@seznam.cz
"""

import random
import time

def welcome():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

def generate_unique_4digit_number():
    while True:
        number = random.randint(1000, 9999)
        digits = str(number)
        if len(set(digits)) == 4:
            return [int(d) for d in digits] #1234 → [1, 2, 3, 4]

def is_valid_input(user_input):
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

def bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    secret_copy = secret[:]
    guess_copy = guess[:]

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            secret_copy[i] = None
            guess_copy[i] = None

    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in secret_copy:
            cows += 1
            secret_copy[secret_copy.index(guess_copy[i])] = None

    return bulls, cows

def print_result(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
    print("-----------------------------------------------")

def main():
    welcome()
    secret_number = generate_unique_4digit_number()
    attempts = 0
    start_time = time.time()

    while True:
        user_input = input("Enter a number:\n-----------------------------------------------\n").strip()
        if not is_valid_input(user_input):
            continue

        guess = [int(d) for d in user_input]
        attempts += 1
        bulls, cows = bulls_and_cows(secret_number, guess)

        if bulls == 4:
            elapsed_time = time.time() - start_time
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print(f"That's amazing!")
            print(f"It took you {elapsed_time:.2f} seconds.")
            break
        else:
            print_result(bulls, cows)

if __name__ == "__main__":
    main()
