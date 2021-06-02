import random

secretNumber = random.randint(1, 100)

print('Hello! What is your name?')
playerName = input()
print(
    playerName + ' I have thought of a random whole number between 1 and 100. You have 10 attempts to guess correctly.')
print('What is your first guess?')

for numberOfGuesses in range(1, 11):
    guessNumber = input()
    if not guessNumber.isnumeric():
        print('Try that one again with integers buddy...')
    elif int(guessNumber) > secretNumber:
        print('That number is too high! Please try again.')
    elif int(guessNumber) < secretNumber:
        print('That number is too low! Please try again')
    else:
        break

if int(guessNumber) == secretNumber:
    print('Congrats ' + playerName + '! You guessed the correct number in ' + str(numberOfGuesses) + ' guess(es)!'
          + ' You must be very smart...')
else:
    print('Wow you idiot... You failed... Better luck next time I guess ¯\_(ツ)_/¯')

# PyCharm says guessNumber and numberOfGuesses can be undefined. I'm not sure how to change that but the game works
# fine regardless.
