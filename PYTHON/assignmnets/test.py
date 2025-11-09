# Get two numbers (-99 to 99)
for i in range(2):
    n = input("Enter a number (-99 to 99): ")
    while n.isdigit() == False or int(n) not in range(-99, 100):
        print("Invalid input! Enter a whole number between -99 and 99.")
        n = input("Enter a number (-99 to 99): ")
    if i == 0:
        num1 = int(n)
    else:
        num2 = int(n)
