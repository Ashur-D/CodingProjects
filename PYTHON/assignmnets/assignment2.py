"""
Q.1 Shipping Calculator
•	Create a program that does the following:
I.	It displays a main menu similar to the one shown below.
1.	Test your addition skills.
2.	Test your subtraction skills.
3.	Test your multiplication skills
4.	Test your exponentiation skills.

II.	It prompts the user to enter two numbers

III. It prompts the user to enter one of the 4 options listed in the menu, then it asks the user to guess the result based on the option selected. If the guess is correct, it displays a message says “Congratulations, you guessed the correct answer!”

IV.	The program performs the corresponding task as given in each option.

V.	It displays the correct outputs.

VI.	It asks the user if they want to play again. The user responds by 'Yes' if they want to continue or 'No' if they do not.

Your program should validate the user inputs, the option and the two numbers so the option must be in the range of 1 to 4, and the numbers must be in the range of -99 and 99.

Your program should ignore the case (upper and lower) in which the user enter Yes or No in VI.
"""
# repeat = 'yes'
# while repeat == 'yes':
#     print("1. Test your addition skills \n2. Test your subtraction skills \n3. Test your multiplication skills \n4. Test your exponentitaion skills")

#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a second number: "))
#     while num1 and num2 not in range(-99,99):
#         num1 = int(input("please try again for the first number: "))
#         num2 = int(input("please try again for the second number: "))

#     choice = int(input("Select from one of the 4 options above with the corresponding number: "))
#     while choice not in range(1,5):
#         choice = int(input("please select again for a number between 1 and 4: "))

#     if choice == 1:
#         num3 = num1 + num2
#     elif choice == 2:
#         num3 = num1 - num2
#     elif choice == 3:
#         num3 = num1 * num2
#     else:
#         num3 = num1 ** num2


#     guess = int(input('Enter your awnser: '))
#     if guess == num3:
#         print('Congratulations, you guessed the correct answer!',num3)
#     else:
#         print('Incorrect')
#     repeat = input('Would you like to play again? ').lower()





"""
Q.2 Working with Lists
- Write a python program that calculates the value of miles per gallons (mpg) for a number of vehicles. It saves every column in a list, total # of lists 4.
- The values of miles and gallons must be validated so they are positive numbers.
- Use a while loop to iterate through the number of the vehicles.
- Your program output should look like the following, use the % operator format operators:

v#	miles		gallons 	mpg
***	****		******	****
1 	210.0 		2.5 		?
2 	900.5 		13.5 		?
3 	515.7 		5.1 		?
4 	780.8 		9.9 		?
5 	666.0 		5.0 		?

"""
# vList = []
# milesList = []
# gallonsList = []
# mpgList = []


# num_vehicles = int(input("Enter the number of vehicles: "))

# i = 0
# while i < num_vehicles:
#     print(f"\nVehicle #{i+1}")
#     break

# miles = 0
# while miles <= 0:
#     miles = float(input("Enter the amount of files driven: "))
#     if miles <= 0:
#         print("please use positive numbers, try again. ")


vehicle_num = []
miles_list = []
gallons_list = []
mpg_list = []

num_vehicles = int(input("Enter the number of vehicles: "))

counter = 0
while counter < num_vehicles:
    print('\nVehicle #'+str(counter+1))

    miles = 0
    while miles <= 0:
        miles = float(input("Enter miles driven: "))
        if miles <= 0:
            print("Miles must be a positive number. Try again.")

    gallons = 0
    while gallons <= 0:
        gallons = float(input("Enter gallons used: "))
        if gallons <= 0:
            print("Gallons must be a positive number. Try again.")

    mpg = miles / gallons

    vehicle_num.append(counter + 1)
    miles_list.append(miles)
    gallons_list.append(gallons)
    mpg_list.append(mpg)

    counter += 1


print("\n%-3s\t%-10s\t%-10s\t%-10s" % ("v#", "miles", "gallons", "mpg"))
print("***\t**********\t**********\t**********")

counter2 = 0
while counter2 < num_vehicles:
    print("%-3d\t%-10.1f\t%-10.1f\t%-10.2f" %
          (vehicle_num[counter2], miles_list[counter2], gallons_list[counter2], mpg_list[counter2]))
    counter2 += 1
