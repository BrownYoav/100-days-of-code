from art import	logo

print(logo)
bidders = {}
more_names = True

while more_names:
	bider = input('What is your name?: ')
	bid = int(input('what is your bid?: $'))
	user_choice = input('Are there any other bidders? Type "yes" or "no".\n')

	bidders[bider] = bid

	if user_choice == 'no':
		more_names = False

print('''------------------------------------------



''')
bidder_bids = list(bidders.values())
bidder_names = list(bidders.keys())

highest_bid = max(bidder_bids)
highest_bid_position = bidder_bids.index(highest_bid)

highest_bidder = bidder_names[highest_bid_position]
print(f'the winner is {highest_bidder} with a bid of ${highest_bid}')