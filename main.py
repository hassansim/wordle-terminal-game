import random

def print_menu():
    print("Let's play Wordle:")
    print("Type a 5 letter word and hit enter!")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

print_menu()