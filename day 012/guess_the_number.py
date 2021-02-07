import random


print('Welcome to the number guessing game.')
print('I\'m thinking of a number between 1 and 100.')
number = random.randint(1,100)

difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
attempts = 5 if difficulty == 'hard' else 10


for i in range(attempts):
    print(f'You have {attempts} attempts to guess the number.')
    while True:
        try:
            guess = int(input('Make a guess: '))
            if guess < 1 or guess > 100:
                raise Exception
            else:
                break
        except:
            print('Enter a valid number between 1 and 100')
    if (guess == number):
        print(f'You got it! The number was {number}')
        break
    else:
        print('Too high.') if guess > number else print('Too low.')
        attempts = attempts - 1
    print('You have run out of guesses, you lose.') if (attempts == 0) else print('Guess again')
