'''
write a python program that calculates the average of a student in a class
The class has 5 students, each having 4 grades of their completed assignments
The program uses a netsted for loop to solve it
'''

asCount = 0 # init a counter

for s in range(1,6):
    total = 0
    asCount = 0
    while asCount < 4: # set a condition
        grade = int(input('Enter the grade of the student ' + str(s) + ': '))
        while grade < 0 or grade > 100:
            grade = int(input('Please enter a valid value: '))
        total += grade # running total for each student to get a total of grades
        asCount += 1 # increment counter
    avg = total/asCount # getting the average of a student
    print('students ' + str(s) + 'has an average of ' + str(avg))
