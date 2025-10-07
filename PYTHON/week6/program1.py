# write a python program that determaines the discount percetanes
# based on age value. Customers get discount of .25 if they are 65 or older or if they
# are less than 12 year olds, then it prints the correct discount pertentage
# make sure to use a logical operator to solve the problem

age = int(input("enter customar age: "))

if age >= 65 or age <= 12:
    discount = 0.25
else:
    discount = 0.0
print("you have a discount of", discount)