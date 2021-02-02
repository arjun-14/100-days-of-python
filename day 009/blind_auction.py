import os
more_bidders = 'yes'
bids = {}
print('Welcome to the secret auction program.')

while(more_bidders == 'yes'):
    user_name = input('What is your name?: ')
    while True:
        try:
            user_bid = int(input('What is your bid?: $'))
            break
        except:
            print('Please enter a valid bid.')
    bids[user_name] = user_bid
    more_bidders = input('Are there any other bidders? Type \'yes\' or \'no\': ')
    clear = lambda : os.system('cls')
    clear()

highest_bidder = max(bids,key=bids.get)
print("The winner is "+highest_bidder+" with a bid of $"+str(bids[highest_bidder]))