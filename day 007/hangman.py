import random
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

display = ['_' for x in chosen_word]

while(True):
    guess = input('Guess a letter : ').lower()

    if guess in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess
    else:
        lives -=1
        print(stages[lives])
        if(lives == 0):
            print('You lose')
            break
        
        
    print(' '.join(display))
    
    if ('_' not in display):
        print('You win')
        break
