import random
import hangman_art as art
import hangman_words as words

word_list = words.word_list
stages = art.stages
lives = 6

chosen_word = random.choice(word_list)


display = ['_' for x in chosen_word]
guessed_letters = []
print(art.logo)
print(' '.join(display))

while(True):
    guess = input('Guess a letter : ').lower()

    if guess in guessed_letters:
        print('You have already guessed the letter '+ guess)
        continue
    else:
        guessed_letters.append(guess)
    
    if guess in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess
        
    else:
        lives -=1
        print('You guessed '+guess+', that\'s not in the word. You lose a life.')
        if(lives == 0):
            print('You lose')
            print('The correct word was '+chosen_word)
            break
    print(' '.join(display))
    print(stages[lives])
            
    if ('_' not in display):
        print('You win')
        break
