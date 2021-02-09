import game_data
import art
import random
import os

print(art.logo)
option_a = random.choice(game_data.data)
option_b = random.choice(game_data.data)
score = 0
game_over = False
user_guess = ''
while True:
    print('') if score == 0 else print(f'You are correct ! Current score: {score}')
    print(f'Compare A: ' + option_a['name'] + ', ' + option_a['description'] + ', from ' + option_a['country'])
    print(art.vs)
    print(f'Against B: ' + option_b['name'] + ', ' + option_b['description'] + ', from ' + option_b['country'])
    while user_guess!= 'a' and user_guess!='b' : 
        user_guess = input('Who has more followers? Please type "A" or "B": ').lower()
    clear = lambda : os.system('cls')

    if user_guess == 'a':
        if option_a['follower_count'] > option_b['follower_count'] :
            score += 1 
        else:
            clear()
            break

    elif user_guess == 'b':
        if option_b['follower_count'] > option_a['follower_count'] :
            score += 1
        else:
            clear()
            break
    
    option_a = option_b
    option_b = random.choice(game_data.data)

    
    clear()
print(f'Thats wrong. Game over! Final score : {score}')