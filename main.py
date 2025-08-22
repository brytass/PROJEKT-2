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

#funkce vygeneruje náhodné 4ciferné číslo s unikátními číslicemi
def generate_unique_4digit_number():
    while True:
        number = random.randint(1000, 9999)     #náhodné číslo od 1000 do 9999
        digits = str(number)                    #převedeme na string, abychom ověřili číslice
        if len(set(digits)) == 4:               #podmínka: všechny číslice musí být unikátní
            return [int(d) for d in digits]     #vrátí list, např. 1234 → [1, 2, 3, 4]

#kontrola, jestli hráč zadal validní vstup
def is_valid_input(user_input):
    if not user_input.isdigit():                #vstup musí být číslo
        print("Please use only digits.")
        return False
    if len(user_input) != 4:                    #musí mít 4 číslice
        print("Please enter exactly 4 digits.")
        return False
    if user_input[0] == "0":                    #nesmí začínat nulou
        print("Number must not start with 0.")
        return False
    if len(set(user_input)) != 4:               #číslice musí být unikátní
        print("Digits must be unique.")
        return False
    return True                                 #pokud vše splní → OK

#výpočet počtu bulls (správná číslice na správném místě)
# a cows (správná číslice, ale na špatném místě)
def bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    secret_copy = secret[:]                     #kopie seznamu, aby se s ním mohlo manipulovat
    guess_copy = guess[:]

    #nejprve hledáme bulls (přesná shoda číslice a pozice)
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            secret_copy[i] = None               #odstraníme z kopie, abychom ho nepočítali dvakrát
            guess_copy[i] = None

    #potom hledáme cows (číslice existuje, ale na jiné pozici)
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in secret_copy:
            cows += 1
            secret_copy[secret_copy.index(guess_copy[i])] = None  # "spotřebujeme" číslici

    return bulls, cows

#funkce pro vypsání výsledku pokusu
def print_result(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"   #správná gramatika
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
    print("-----------------------------------------------")

#hlavní logika hry
def main():
    welcome()                                      
    secret_number = generate_unique_4digit_number()
    attempts = 0
    start_time = time.time()      #start časomíry

    #herní smyčka
    while True:
        #hráč zadá tip
        user_input = input("Enter a number:\n-----------------------------------------------\n").strip()
        
        #kontrola vstupu
        if not is_valid_input(user_input):
            continue

        guess = [int(d) for d in user_input]        #převod vstupu na list čísel
        attempts += 1
        bulls, cows = bulls_and_cows(secret_number, guess)

        #pokud hráč uhodl všechny číslice správně
        if bulls == 4:
            elapsed_time = time.time() - start_time
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print(f"That's amazing!")
            print(f"It took you {elapsed_time:.2f} seconds.")
            break                                   
        else:
            print_result(bulls, cows)             

#spuštění hry
if __name__ == "__main__":
    main()
