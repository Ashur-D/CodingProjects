# using global and local var

num1 = 7 # global variable

def addNums(x):
    sum1 = x + 13 # local variable
    num1 = 5
    print('Inside addNums num1:',num1)
    print(sum1)

def main():
    x = int(input('Enter a value for x: ')) # local variable
    print('Inside main() num1:',num1)
    addNums(x) # calling statement

if __name__ == '__main__':
    main()

# passing parameters by value means we are copying it to the function we want,
# the values changed on the new function do now affect the previous ones.

# passing by refrence, means to pass a refrence in the memory. Unlike passing by value,
# when we change the value of the refrence it changes it for the previous one. It has a memory address.

# These 2 ways depend on the interpreter. The above is for python.
