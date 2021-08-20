import random

number = random.randint(1, 10)

player_name = input("Hello! What's your name?")

print('Okay! ' + player_name + 'I am guessing a number between 1 and 10.')

number_of_guesses = 0

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number: 
        print('Try again! Your guess is too low.')
    if guess > number: 
        print('Almost! Your guess is too high...')
    if guess == number: 
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('Bummer! You did NOT guess the number. It was ' + str(number))
        

