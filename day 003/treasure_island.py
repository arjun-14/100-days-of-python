print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print('You are at a cross road. Where do you want to go? Type "left" or "right"')
left_or_right = input().lower()
if(left_or_right != 'left'):
  print('You fell into a hole. Game over.')
else:
  print('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.')
  swim_or_wait = input().lower()
  if(swim_or_wait != 'wait'):
    print('You were attacked by a trout. Game over.')
  else:
    print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
    colour = input().lower()
    if(colour == 'red'):
      print('You were burned by fire. Game over.')
    elif(colour == 'blue'):
      print('You were eaten by beasts. Game over.')
    elif(colour == 'yellow'):
      print('You win!')
    else:
      print('You lose.Game over.')
