'''
write a python program that randomly generates a number within a specific range. Prompt the user to guess a number. Let the user try a number of times. Inform user at what time they were able to guess. 

'''

import random

guesses = 10
x = random.randint(1,20) # gives us a random int between 1-20
print(x)

while guesses > 0:
    guess = input('Guess a number between 1 and 20: ')
    if guess == str(x):
        print('You guessed the correct number on guess',guesses)
        break
    else:
        print('Wrong! try again you have', guesses, 'tries')
    guesses -= 1
print('thanks for playing!')
