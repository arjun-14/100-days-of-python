import random

if __name__ == "__main__":
    try:
        user_score = 0
        computer_score = 0
        rock = '''
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
        win_condition = [(0, 2), (1, 0), (2, 1)]
        while True:
            try:
                user_choice = int(
                    input('What do you choose ? Type 0 for rock, 1 for paper, 2 for scissors \n'))
                if (user_choice > 2 or user_choice < 0):
                    raise Exception()
                print(options[user_choice])
            except Exception:
                print(
                    f"Your score: {user_score}, Computer score: {computer_score}.")
                print('Invalid choice, Ctrl+C to exit.')
                continue
            print('Computer choose :')
            computer_choice = random.randint(0, 2)
            print(options[computer_choice])
            if user_choice == computer_choice:
                print('Draw, Ctrl+C to exit.')
                print(
                    f"Your score: {user_score}, Computer score: {computer_score}.")
            elif (user_choice, computer_choice) in win_condition:
                user_score = user_score+1
                print('You win, Ctrl+C to exit.')
                print(
                    f"Your score: {user_score}, Computer score: {computer_score}.")
            else:
                computer_score = computer_score+1
                print('You lose, Ctrl+C to exit.')
                print(
                    f"Your score: {user_score}, Computer score: {computer_score}.")
    except KeyboardInterrupt:
        print(f"Your score: {user_score}, Computer score: {computer_score}.")
        print("Exiting...")
    except Exception:
        raise
