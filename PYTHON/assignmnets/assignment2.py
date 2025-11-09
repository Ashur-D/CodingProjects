'''
Q.1 Shipping Calculator
•	Create a program that does the following:
I.	It displays a main menu similar to the one shown below.
1.	Test your addition skills.
2.	Test your subtraction skills.
3.	Test your multiplication skills
4.	Test your exponentiation skills.

II.	It prompts the user to enter two numbers

III.	It prompts the user to enter one of the 4 options listed in the menu, then it asks the user to guess the result based on the option selected. If the guess is correct, it displays a message says “Congratulations, you guessed the correct answer!”

IV.	The program performs the corresponding task as given in each option.

V.	It displays the correct outputs.

VI.	It asks the user if they want to play again. The user responds by 'Yes' if they want to continue or 'No' if they do not.

Your program should validate the user inputs, the option and the two numbers so the option must be in the range of 1 to 4, and the numbers must be in the range of -99 and 99.

Your program should ignore the case (upper and lower) in which the user enter Yes or No in VI.
'''


print('1. Test your addition skills \n2. Test your subtraction skills \n3. Test your multiplication skills \n4. Test your exponentitaion skills')

num1 = int(input('Enter a number '))
num2 = int(input('Enter a second number '))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
expo = num1 ** num2

choice = int(input('Select from one of the 4 options above with the corresponding number: '))

while choice == 1 or 2 or 3 or 4:
    if choice == 1:
        input('based on the 2 numbers you gave above, what will the outcome be? ')
        if num1 + num2 == add:
            print('Congratulations, you guessed the correct answer! it was' , add)
            choice2 = input('would you like to play again? ').lower
            if choice2 == 'yes':
                continue
            else:
                print('Thanks for playing')
                break
        else:
            break



    else:
        choice = int(input('Please try again and select a number from 1-4: '))



















'''
Q.2 Working with Lists
Write a python program that calculates the value of miles per gallons (mpg) for a number of vehicles. It saves every column in a list, so the total number of lists crated in your program is four. The values of miles and gallons must be validated so they are positive numbers.
Use a while loop to iterate through the number of the vehicles.
Your program output should look like the following, use the % operator format operators:

v#	miles		gallons 	mpg
***	****		******	****
1 	210.0 		2.5 		?
2 	900.5 		13.5 		?
3 	515.7 		5.1 		?
4 	780.8 		9.9 		?
5 	666.0 		5.0 		?

'''



