'''
write a python program that calcualtes the gross pays of a few employees.
Define a function, processPay that performs the calc and prints out.
the processPays() functions runs a loop to perform the calcuations
the main function gets the number of employees
''' # ask someone for the rest

def processPays(empCount):
    count = 0

    while count < empCount:
        hrs , payRate = input('Enter your hours and payrate: ').split()
        hrs , payRate = float(hrs), float(payRate)
        gross = hrs * payRate
        print(f'gross pay of employee {count + 1}: ${gross}')
        count += 1

def main():
    empCount = int(input('Enter the number of employees: '))
    processPays(empCount)

if __name__ == '__main__': # givin on the final exam
    main()
