count = 0 # initialize a counter at 0
total = 0 # initialize total that holds the total value 
students = int(input("enter the number of students: "))

while count < students: # set a condition to control the loop
    grades = int(input("enter the grade for this student: "))
    total += grades #total += weight # can also be written as total = total + weight
    print('student ' + str(count + 1) + ' has a grade of ' + str(grades)) # note-to-self, + can be replaced for commas (expect the count + 1)
    count += 1 # update the value of count  / can also be displayed as count = count + 1
#print('The total of all  of all your shipments are ', total)
print('the average of all grades were', round(total/count,2))