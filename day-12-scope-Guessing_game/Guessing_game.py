from art import *
from random import *

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10
print(logo)
print('Welcome to the guessing game!')
difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
if difficulty == 'easy':
	lives = EASY_LEVEL_TURNS 
else:
	lives = HARD_LEVEL_TURNS
print(f'I am thinking of a number between 1 and 100 you have {lives} attempts to guess it')

rand_num = randint(1, 100)
result = ''

def compare(generated_numb, gussed_numb):
	global lives
	outcome = ''
	if generated_numb == gussed_numb:
		outcome = 'You are correct!!!'
	elif generated_numb > gussed_numb:
		outcome = 'Too low'
		lives -= 1

	else:
		outcome = 'Too high'
		lives -= 1
		
	return outcome


while result != 'You are correct!!!' and lives > 0:
	print(f'you have {lives} attemps remaining')
	guess = int(input('make a guess: '))
	result = compare(rand_num, guess)
	print(result)
if result != 'You are correct!!!':
	print('you lose!!, loser')