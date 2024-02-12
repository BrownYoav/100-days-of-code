from random import *
from art import *
from game_data import *



		# 'name': 'Instagram',
        # 'follower_count': 346,
        # 'description': 'Social media platform',
        # 'country': 'United States'



def new_round(people_list:list,prev_winner = None) -> dict and dict:
	"""	gets list of data and returns two peapleo in the form of a dictionary """
	if prev_winner is None:
		a = choice(people_list)
		b = choice(people_list)
	else:
		a = prev_winner
		b = choice(people_list)
	return a,b 

def compare(person1:dict, person2:dict) -> str:
	"""gets two people and returns the person with more followers"""
	if person1['follower_count'] > person2['follower_count']:
		more_followed = person1
	else:
		more_followed = person2


	return more_followed

def beautify(person:dict):
	new_person = f"{person['name']}, {person['description']}, {person['country']}."
	return new_person


def higher_lower_gane():
	people = data
	score = 0
	perA,perB = new_round(people)
	game_on =True
	user_feedback =''

	
	while game_on:
		print('=========================new round====================================================')
		print(logo)
		print(user_feedback)
		print(f'Compare A: {beautify(perA)}')
		print(vs)
		print(f'Against B: {beautify(perB)}')

		#user choice
		user_input = input("Who has more followers? Type 'A' or 'B': ")
		
		#determine winner and correct answer
		winner = compare(perA, perB)
		if winner == perA:
			correct_ans = 'a'
		else:
			correct_ans = 'b'
		#determine wehteher user was right
		if user_input == correct_ans:
			score += 1
			user_feedback = f"You're right! Current score: {score}"
			print(f'this is first person ({beautify(perA)}) this is second person ({beautify(perB)}) and this is the winner ({beautify(winner)}) ')
			perA,perB = new_round(people,winner)
			
		else:
			user_feedback = f"Sorry, that's wrong. Final score: {score}"
			game_on = False
			print(user_feedback)

higher_lower_gane()