hours = 0
wage = 0

keepGoing = 'y'
while keepGoing == 'y' or keepGoing == 'yes':
    hours = int(input('Enter your hours: '))
    wage = float(input('Enter your wage: '))

    while hours < 0:
        hours = int(input('please try again and enter your hours: '))

    while wage < 0:
        wage = float(input('please try again and enter your wage: '))

    gross = hours * wage
    taxAmount = gross * 0.13
    net = gross - taxAmount

    print(f'your net amount is {net}')
    keepGoing = input('Would you like to try again? ').lower()
print('thanks')
