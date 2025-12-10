# prompt the user to enter a number of courses
# in a loop, prompt the user to enter the courses (like python,java,c)
# append the classes to a list
# make sure to validate the inputs

input1 = int(input('Enter the number of courses: '))
while input1 < 0:
    input1 = int(input('please try again and enter a number: '))

classes = []
for i in range(input1):
    input2 = input(f'Enter course {i+1}: ')
    classes.append(input2)

print(classes)

'''
add an extra line to the file
remove a line from a file
for mc questions are after the midterm
'''
