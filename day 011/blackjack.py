import random

player_decision = input('Do you want to play a game of blackjack? Press "y" to start, "n" to exit: ');
cards_user_total = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cards_computer_total = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

while sum(computer_cards) < 17:
    computer_new_card = random.choice(cards_computer_total)
    computer_cards.append(computer_new_card)
    cards_computer_total.remove(computer_new_card)

def win_condition():
    if sum(user_cards) == 21:
        return 'won'
    if sum(user_cards) > 21:
        return 'lost'
    if sum(user_cards) < 21:
        return 'continue'

if player_decision == 'y':
    
    for i in range(2):
        user_new_card = random.choice(cards_user_total)
        user_cards.append(user_new_card)
        cards_user_total.remove(user_new_card)
    
    print(f'Your cards: {user_cards}, current score: {sum(user_cards)}')
    print(f'Computer\'s first card: {computer_cards[0]}\n')

    if win_condition() == 'won':
        print(f'Your final hand: {user_cards}, final score: {sum(user_cards)}')
        print(f'Computer\'s final hand: {computer_cards}, final score: {sum(computer_cards)}')
        print('You win!') if sum(computer_cards) < 21 else print('Draw')

    if win_condition() == 'continue':
        while True:
            user_input = input('Type "y" to get another card, type "n" to pass: ') 
            
            if user_input == 'y':
                user_new_card = random.choice(cards_user_total)
                if user_new_card == 11:
                    if (sum(user_cards) + 11) > 21:
                        user_cards.append(1)
                    else:
                        user_cards.append(11)
                else:
                    user_cards.append(user_new_card)
                cards_user_total.remove(user_new_card)
             
                if win_condition() == 'won' or win_condition() == 'lost':
                    print(f'Your final hand: {user_cards}, final score: {sum(user_cards)}')
                    print(f'Computer\'s final hand: {computer_cards}, final score: {sum(computer_cards)}')
                    print('You win!') if win_condition() == 'win' else print('Bust! You lose')
                    break
                
                else:
                    print(f'Your cards: {user_cards}, current score: {sum(user_cards)}')
                    print(f'Computer\'s first card: {computer_cards[0]}\n')

            else:                     
                print(f'Your final hand: {user_cards}, final score: {sum(user_cards)}')
                print(f'Computer\'s final hand: {computer_cards}, final score: {sum(computer_cards)}')
                
                if sum(computer_cards) > 21:
                    print('Computer went over. You win!')
                elif sum(computer_cards) > sum(user_cards):
                    print('You lose!')
                elif sum(computer_cards) == sum(user_cards):
                    print('Draw')
                else:
                    print('You Win!')
                break
                    
                    
                  
        
     
        