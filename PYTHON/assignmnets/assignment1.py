# Q1
print("Net Pay Calculator")

hoursWorked = int(input("Enter your hours worked: "))
payRate = float(input("Enter your pay rate: "))
taxPercent = int(input("Enter your tax percent: "))
vacationPay = float(input("Enter your vacation pay: "))

gross = hoursWorked * payRate
taxAmonut = gross * taxPercent / 100
netAmount = gross - taxAmonut + vacationPay

print('%s%.3f%s%.3f%s%.3f'%("gross:$",gross," \ntax before vacation:$",taxAmonut," \nnet amount:$",netAmount))


# Q2
cents = int(input("Enter number of cents (0-99): "))

quarters = cents // 25  # // is floor division. It divides and only keeps the whole number, ignoring any remainder.
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents 

print('%s%5d%s%7d%s%5d%s%5d'%("Quarter:",quarters ,"\nDimes:",dimes,"\nNickels:",nickels,"\nPennies:",pennies,))


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


# Q3.3

num1 = 5.29689
num2 = 12.67908
print('%20.3f%20.3f'%(num1,num2))



# Q3.4
name = input("enter store manager name: ")
firstSale = float(input("Enter first sales amount: ")) # use the float before taking the user input
secondSale = float(input("Enter second sales amount: "))
print(f"{name}, has logged his first sales amount as ${firstSale:.2f} and his second sales amount as ${secondSale:.2f}") 