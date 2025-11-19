# a program that calculates the value of mpg using a user defiened function named, calcMPG

def calcMPG():
    miles, gallons = input('Enter miles and gallons: ').split()
    miles, gallons = int(miles), int(gallons)

    mpg = miles/gallons

    return mpg # returning the value of mpg to the calling statement

# calling the function to be executed by the interpreter, it execs line 12 first.
# interpeter jumps from 13 to line 3
# line 9 is the last line to exec

mpg = calcMPG() # python looks for the calling statement first
print('mpg: ',round(mpg,2))
# print('mpg: ' + str(round(mpg,2)))

print('mpg: ' + str(round(calcMPG(),2)))
# print('mpg ' , (round(calcMPG(),2)))
