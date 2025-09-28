# getting multiple inputs from the user in one input statement

# we can assign multiple variable to the users input, along with using the .split function we split each user input by a space so that its not one single digit but 3
grade1, grade2, grade3 = input('Enter the three grades(seperate thme with a single space):').split()

# cast each variable to an int
grade1, grade2, grade3 = int(grade1), int(grade2), int(grade3),

avg = (grade1 + grade2 + grade3)/3

print('average =', round(avg, 2))