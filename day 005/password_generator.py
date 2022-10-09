import random
import string


def generate_password(letters, symbols, numbers):
    try:
        random_letters = [random.choice(string.ascii_letters)
                          for n in range(letters)]
        random_symbols = [random.choice(string.punctuation)
                          for n in range(symbols)]
        random_numbers = [random.choice(string.digits) for n in range(numbers)]
        password = random_letters + random_symbols + random_numbers
        random.shuffle(password)
        password = ''.join(password)
        return password
    except Exception:
        raise


if __name__ == "__main__":
    default_num_letters = 8
    default_num_symbols = 2
    default_num_numbers = 4
    try:
        print('Welcome to PyPassword Generator.')
        print(
            f"Example: {generate_password(letters=default_num_letters,symbols=default_num_symbols,numbers=default_num_numbers)}, Ctrl+C to Exit.")
        while True:
            try:
                letters = int(
                    input('How many letters would you like in your input?\n'))
            except Exception:
                print(
                    f'invalid number of letters, setting default to {default_num_letters}')
                letters = default_num_letters

            try:
                symbols = int(input('How many symbols would you like?\n'))
            except Exception:
                print(
                    f'invalid number of symbols, setting default to {default_num_symbols}')
                symbols = default_num_symbols

            try:
                numbers = int(input('How many numbers would you like?\n'))
            except Exception:
                print(
                    f'invalid number of numbers, setting default to {default_num_numbers}')
                numbers = default_num_numbers

            password = generate_password(
                letters=letters, symbols=symbols, numbers=numbers)

            print(f'Here is your password: {password}, Ctrl+C to Exit.')
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception:
        raise
