import sys
import random

def main():
    #get level
    level = get_level()

    # generate random value
    right_guess =  random.randint(1, level)

    # play game
    guess_game(right_guess)

def get_level():
    while True:
        n = input('Level: ')
        try:
            n = int(n)
        except ValueError:
            pass
        else:
            if n >= 1: 
                return n


def guess_game(right_guess: int):
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
        except:
            pass
        else:
            if guess < right_guess:
                print('Too small!')
            elif guess > right_guess:
                print('Too large!')
            else: 
                print('Just right!')
                return
