import random
import os

from art import logo

answer = random.choice(range(1, 101))

def clear():
    os.system('clear')

def check_valid_answer():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        live = 0

        if level == 'easy':
            live = 10
            break
        elif level == 'hard':
            live = 5
            break
    
    return live

def guess_number(live):
    if live == 1:
        print(f'You have {live} attemp to guess the number')
    else:
        print(f'You have {live} attemps to guess the number')

    number_guess = int(input('Make a guess: '))

    return number_guess

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

live = check_valid_answer()

number_guess = guess_number(live)

while number_guess != answer:
    if number_guess < answer:
        print("too low")
        live -= 1
        number_guess = guess_number(live)
        if live == 0:
            break 
    elif number_guess > answer:
        print("too high")
        live -= 1
        number_guess = guess_number(live)
        if live == 0:
            break 
    elif number_guess == answer: 
        break

if number_guess == answer: 
    print(f"You got it! The answer was {answer}.")

if live == 0:
    print("You lose")