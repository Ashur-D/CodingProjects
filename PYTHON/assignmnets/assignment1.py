# Q1
print("Net Pay Calculator")

hoursWorked = int(input("Enter your hours worked: "))
payRate = float(input("Enter your pay rate: "))
taxPercent = int(input("Enter your tax percent: "))
vacationPay = float(input("Enter your vacation pay: "))

gross = hoursWorked * payRate
taxAmountBeforeVacation = gross * payRate / 100
netAmount = gross - taxAmountBeforeVacation + vacationPay

print("Your gross amount is: ", round(gross, 2))
print("Your tax amount before vacation is: ", round(taxAmountBeforeVacation, 2))
print("Your net amount is: ", round(netAmount, 2))




# Q2
cents = int(input("Enter number of cents (0-99): "))

quarters = cents // 25  # // is floor division. It divides and only keeps the whole number, ignoring any remainder.
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents 

print("Quarters: " + str(quarters), "Dimes: " + str(dimes), "Nickels: " + str(nickels), "Pennies: " + str(pennies), sep="\n")


# Q3

# Q3.1
print("If you cant handle me, \n you at my worst then you \t dont deserve me at my \'best.\'")


# Q3.2
str1 = 'absherd centdanenz'

sheridan = str1[2:6] + 'i' + str1[12:15]
sheridan2 = sheridan[-1]

print(sheridan)
print(sheridan.endswith('n'))


print(sheridan[0:2] + ' ' + sheridan[3:8])

# Q3.4
name = input("enter store manager name: ")
firstSale = input("Enter first sales amount: ")
secondSale = input("Enter second sales amount: ")