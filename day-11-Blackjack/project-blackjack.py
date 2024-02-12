
from random import *
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
player_hand = []
dealer_hand = []
play_again = 'y'
deal = 'y'

def deal_card(hand:list, pack_of_cards:list):
	hand.append(choice(pack_of_cards))

def make_hand(hand:list, pack_of_cards:list):
	deal_card(hand,pack_of_cards)
	deal_card(hand,pack_of_cards)

def show_hands(hand1:list, hand2:list):
	score1 = tally_hand(hand1)
	score2 = tally_hand(hand2)

	print(f'your cards are: {hand1} your score is {score1}')
	print(f"the dealer's cards are: {hand2} dealer's current score is {score2} ")

def tally_hand(hand):
	if (11 in hand) and (sum(hand) > 21):
		# 11 becomes 1
		position = hand.index(11)
		hand[position] = 1
		# now call the function again
		result = tally_hand(hand)
		return result
	else:
		return sum(hand)

def end_of_game(hand1, hand2):
	sum_player = tally_hand(hand1)
	sum_dealer = tally_hand(hand2)
	print('=======================================')
	if (sum_dealer < sum_player <= 21) or (sum_dealer > 21 and sum_player <= 21):
		print(f'You win!!') 
	else:
		print('You lose!!')

def comp_turn(user_hand, comp_hand) -> None:
	comp_score = tally_hand(comp_hand)
	user_score = tally_hand(user_hand)
	
	if user_score > 21 or comp_score > user_score:
		return

	while comp_score < user_score and comp_score < 21:
		deal_card(comp_hand, deck)
		comp_score = tally_hand(comp_hand)
		show_hands(user_hand, comp_hand)
	return
		


def black_jack():
	play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
	while play_again == 'y':
		print(logo)
		make_hand(player_hand, deck)
		deal_card(dealer_hand, deck)

		show_hands(player_hand, dealer_hand)

		if tally_hand(player_hand) < 21:
			deal = input("Type 'y' to get another card, type 'n' to pass: ")

		while deal == 'y' and (tally_hand(player_hand)<21):
			print('--------------------------------------------------------------------')
			deal_card(player_hand, deck)
			show_hands(player_hand, dealer_hand)
			if tally_hand(player_hand) < 21:
				deal = input("Type 'y' to get another card, type 'n' to pass: ")
			else:
				deal = 'n'


		comp_turn(player_hand, dealer_hand)

		end_of_game(player_hand, dealer_hand)

		player_hand.clear()
		dealer_hand.clear()
		play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")






black_jack ()




