# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2= name2.lower()

tens = 0 
units = 0

var_tens = 'true'
var_units = 'love'

for letter in var_tens:
	if letter in name1 or name2:
		tens += name1.count(letter) + name2.count(letter)

for letter in var_units:
	if letter in name1 or name2:
		units += name1.count(letter) + name2.count(letter)

score = str(tens) + str(units)

if int(score) < 10 or int(score) > 90:
	print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= int(score) <= 50:
	print(f'Your score is {score}, you are alright together.')
else:
	print(f'Your score is {score}.')