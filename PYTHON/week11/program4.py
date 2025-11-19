'''
write a program that displays students last name and average of 3 quizzes
in the main function > get the 4 inputs and pass the inputs
call another function, calcAVG and pass the 4 parameters
In calcAVG, calculate the average of 3 grades
Lastly print the students name and average
'''

def __main__():
    lastName, grade1, grade2, grade3 = input("Enter your name followed by your 3 quizzes (with a space): ").split()
    grade1,grade2,grade3 = int(grade1),int(grade2),int(grade3)
    average = calcAVG(grade1,grade2,grade3)
    print(f'{lastName}, your average is {average}')


def calcAVG(grade1,grade2,grade3):
    average = (grade1+grade2+grade3)/2
    return average

if __name__ == "__main__":
    __main__()
