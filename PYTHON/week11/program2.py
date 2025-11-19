def calcMPG():
    miles, gallons = input('Enter miles and gallons: ').split()
    miles, gallons = int(miles), int(gallons)
    mpg = miles/gallons
    return mpg

def main(): # Since we have a main function, this is the first line that gets exec.
    mpg = calcMPG()
    print('mpg: ',round(mpg,2))
    # print('mpg: ' + str(round(mpg,2)))

    print('mpg: ' + str(round(calcMPG(),2)))
    # print('mpg ' , (round(calcMPG(),2)))

if __name__ == "__main__": # if the main function is in the program, we want to run it. note: main should be at the bottom
    main()

# the order of parameters passed must match the amount,order and data types.
