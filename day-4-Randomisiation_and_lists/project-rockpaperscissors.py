import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = int(input("what do you choose? rock 0, paper 1, scissors 2? "))
computer = random.randint(0, 2)

hands = [rock , paper, scissors]

print(f'You chose: \n {hands[player]}')
print(f'computer chose: \n {hands[computer]}')

if player == 0:
    if computer == 0:
	    result = 'drew'
    elif computer == 1:
        result = 'lost'
    else:
        result = 'won'
elif player == 1:
    if computer == 0:
    	result = 'won'
    elif computer == 1:
        result = 'drew'
    else:
        result = 'lost'
else:
    if computer == 0:
    	result = 'lost'
    elif computer == 1:
        result = 'won'
    else:
        result = 'drew'


print(f'you {result}')