print('Welcome to the bill calculator.')
totalBill = float(input('What was the total bill? $'))
noOfPeople = float(input('How many people to split the bill? '))
percentage = float(
    input('What percentage tip would you like to give? 10, 12 or 15? '))
amountToPay = round(
    totalBill / noOfPeople + totalBill / noOfPeople * percentage / 100, 2)
print(f'Each person should pay: ${amountToPay}')
