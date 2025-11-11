# write a python program that calculates the average of 5 grades and prints out the value of the average.
# It checks the grades and makes sure only valid grades are counted.

sumGrade = 0.0
countV = 0

grades = [90.5,8.1,95.0,84.7,89.9,-30.2,1001]

for grade in grades:
    if grade > 0 and grade <= 100:
        sumGrade += grade
        countV += 1
avg = sumGrade/countV # the execption must be handled
print('%10d%10.2f'%(countV,avg))
