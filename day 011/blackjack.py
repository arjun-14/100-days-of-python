import random

player_decision = input('Do you want to play a game of blackjack? Press "y" to start, "n" to exit: ');
cards_user_total = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cards_computer_total = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

if player_decision == 'y':
    user_first_card = random.choice(cards_user_total)
    user_cards.append(user_first_card)
    cards_user_total.remove(user_first_card)
    
    user_second_card = random.choice(cards_user_total)
    user_cards.append(user_second_card)
    cards_user_total.remove(user_second_card)

    computer_first_card = random.choice(cards_computer_total)
    computer_cards.append(computer_first_card)
    cards_computer_total.remove(computer_first_card)
    
    computer_second_card = random.choice(cards_computer_total)
    computer_cards.append(computer_second_card)
    cards_computer_total.remove(computer_second_card)
    
    print(f'Your cards: {user_cards}, current score: {sum(user_cards)}')
    print(f'Computer\'s first card: {computer_cards[0]}')

    first_pass = input('Type "y" to get another card, type "n" to pass: ')