import random
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)

guess = input('Guess a letter : ')

for i in chosen_word:
    if i == guess:
        print('Right')
    else:
        print('Wrong')
