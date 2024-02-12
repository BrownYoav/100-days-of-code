#Password Generator Project
from random import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
##Eazy Level - Order not randomised:
##e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# len_password = nr_letters + nr_numbers +nr_symbols
# password = []

# for number in range(nr_letters):
# 	rnd_letter = letters[randint(0, 51)]
# 	password.append(rnd_letter)

# for number in range(nr_numbers):
# 	rnd_number = numbers[randint(0, 9)]
# 	password.append(rnd_number)

# for number in range(nr_symbols):
# 	rnd_symbol = symbols[randint(0, 8)]
# 	password.append(rnd_symbol)

# print(password)
# password = "".join(password)

# print(str(password))

##Hard Level - Order of characters randomised:
##e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

len_password = nr_letters + nr_numbers +nr_symbols
password = []

for char in range(nr_letters):
	rnd_letter = choice(letters)
	password.append(rnd_letter)

for number in range(nr_numbers):
	rnd_number = choice(numbers)
	password.append(rnd_number)

for symbol in range(nr_symbols):
	rnd_symbol = choice(symbols)
	password.append(rnd_symbol)


shuffle(password)
password = "".join(password)
print(password)
