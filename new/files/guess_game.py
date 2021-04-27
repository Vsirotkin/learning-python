# This is a guess the number game.
import random

secretNumber = random.randint(1, 6)
print('I am thinking of a number between 1 and 5.')
guesses_stop = 5

# Ask the player to guess 5 times.
for guessesTaken in range(1, 5):
    print(secretNumber)
    guess = int(input('Take a guess: '))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')

    if guess == secretNumber:
        print(f'Good job! You guessed my number in  {guessesTaken} guesses!')
        break
    else:
        print(f'Nope. Take another try. You still have {guesses_stop - guessesTaken} guesses.')