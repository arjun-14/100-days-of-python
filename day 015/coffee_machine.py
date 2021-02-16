menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "report" : {},
    "exit" : {}
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarter = 0.25
dime = 0.1
nickle = 0.05
penny = 0.01

while True:
    user_choice = input('What would you like? (espresso/latte/cappuccino/exit): ').lower()
    while user_choice not in menu :
        user_choice = input('Please select a proper option. What would you like? (espresso/latte/capuccino/exit): ').lower()
    
    if user_choice == 'exit':
        break
    
    if user_choice == 'report':
        print('water: ' + str(resources["water"]))
        print('milk: ' + str(resources["milk"]))
        print('coffee: ' + str(resources["coffee"]))
        continue

    if (resources['water'] >= menu[user_choice]['ingredients']['water']) and (resources['milk'] >= menu[user_choice]['ingredients']['milk']) and (resources['coffee'] >= menu[user_choice]['ingredients']['coffee']) :    
        print('Please insert coins.')
        while True:
            try:
                quarters = int(input('how many quarters?: '))
                dimes = int(input('how many dimes?: '))
                nickles = int(input('how many nickles?: '))
                pennies = int(input('how many pennies?: '))
                break
            except:
                print('Please enter a number.')



        total_amount = quarter * quarters + dime * dimes + nickle * nickles + penny * pennies
        change = round(total_amount - menu[user_choice]["cost"], 2)

        if change > 0 :
            print(f'Here is ${change} in change.')
            print(f'Here is your {user_choice} ☕ Enjoy!')
        elif change < 0 :
            print('Sorry that\'s not enough money. Money refunded.')
            continue
        else:
            print(f'Here is your {user_choice} ☕ Enjoy!')

        resources['water'] = resources['water'] - menu[user_choice]['ingredients']['water']
        resources['milk'] = resources['milk'] - menu[user_choice]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - menu[user_choice]['ingredients']['coffee']
    
    else:
        depleted_resources = []
        if resources['water'] < menu[user_choice]['ingredients']['water'] : depleted_resources.append('water')
        if resources['milk'] < menu[user_choice]['ingredients']['milk'] : depleted_resources.append('milk')
        if resources['coffee'] < menu[user_choice]['ingredients']['coffee'] : depleted_resources.append('coffee')
        print('Sorry there is not enough '+ ', '.join(depleted_resources))