# write a python program that takes the hours worked and pay rate as user inputs.
# it calculates the gross amount and prints it out.
# make sure the program validates the two user inputs before computing the gross value


hours, payRate = input('Enter your hours and payrate: ').split()
hours, payRate = int(hours), float(payRate)

while hours <= 0:
    print('this is an invalid value, try again.')
    hours = int(input('Enter hours worked: '))
    
while payRate <= 0:
    print('this is an invalid value, try again.')
    payRate = float(input('Enter your payRate: '))

gross = hours * payRate
print(f'gross amount: ${gross}')

