import random
import string

print('Welcome to PyPassword Generator.')
letters = int(input('How many letters would you like in your input?\n'))
symbols = int(input('How many symbols would you like?\n'))
numbers = int(input('How many numbers would you like?\n'))

random_letters =[random.choice(string.ascii_letters) for n in range(letters)]
random_symbols = [random.choice(string.punctuation) for n in range(symbols)]
random_numbers = [random.choice(string.digits) for n in range(numbers)]
password = random_letters + random_symbols + random_numbers

random.shuffle(password)
print(''.join(password))
