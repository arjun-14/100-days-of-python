import os

repeat = ''
operand = ''
ans = 0

while(repeat!= 'e'):
    if(repeat == 'y'):
        operator1 = ans
    else:
        clear = lambda : os.system('cls')
        clear()
        while True:
            try:
                operator1 = float(input('What\'s the first number?: '))
                break
            except:
                print('Enter a valid number.')
        print('+\n-\n*\n/\n')
    
    operand = ''
    while(operand!='+' and operand!='-' and operand!='*' and operand!='/'):
        operand = input('Pick an operation: ')
        if(operand!='+' and operand!='-' and operand!='*' and operand!='/'):
            print('Invalid operand.')
    while True:
            try:
                operator2 = float(input('What\'s the next number?: '))
                break
            except:
                print('Enter a valid number.')
    
    ans = (operator1 + operator2) if operand == '+' else ((operator1 - operator2) if operand == '-' else(operator1 * operator2 if operand == '*' else (operator1 / operator2)))

    print(f'{operator1} {operand} {operator2} = {round(ans,2)}')
    repeat = ''
    
    while(repeat!='y' and repeat!='n' and repeat!='e'):
        repeat = input(f'Type "y" to continue calculating with {round(ans,2)}, type "n" to start a new calculation, type "e" to exit: ')
        if(repeat!='y' and repeat!='n' and repeat!='e'):
            print('Invalid input')
