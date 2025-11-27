def processGrades2(grades_count):
    count = 0
    theSum = 0
    countPassing = 0

    while count < grades_count:
        grade = float(input('Enter a grade: '))
        if grade >= 50 and grade <= 100:
            theSum += grade # running total
            countPassing += 1 # good counter
        count += 1 # general counter
    return theSum, countPassing


def main():
    grades_count = int(input('Enter the number of grades you have: '))
    while grades_count < 0:
        grades_count = int(input('Please enter a valid amount of grades: '))

    passing = processGrades2(grades_count)
    average = passing[0]/passing[1] # unpacks it as a tuple, and divides
    print(f'the average of the passing grades are {average}')

if __name__ == '__main__':
    main()
