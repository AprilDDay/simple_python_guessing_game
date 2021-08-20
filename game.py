import random

number = random.randint(1, 10)

player_name = input("Hello! What's your name?")

print('Okay! ' + player_name + 'I am guessing a number between 1 and 10.')

while number_of_guesses < 5:
    guess = 