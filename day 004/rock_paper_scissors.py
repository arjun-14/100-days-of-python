import random

rock ='''
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
options = [rock, paper, scissors]

win_condition = [(0,2),(1,0),(2,1)]

user_choice = int(input('What do you choose ? Type 0 for rock, 1 for paper, 2 for scissors \n'))
print(options[user_choice])

print('Computer choose :')
computer_choice = random.randint(0, 2)
print(options[computer_choice])

if(user_choice > 2 or user_choice < 0):
    print('Invalid choice')
elif(user_choice == computer_choice):
  print('You draw')
elif (user_choice, computer_choice) in win_condition:
  print('You win')
else:
  print('You lose')
