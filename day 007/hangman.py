import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = ['_' for x in chosen_word]

while(True):
    guess = input('Guess a letter : ').lower()

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
        
    print(display)
    
    if ('_' not in display):
        print('You win')
        break
