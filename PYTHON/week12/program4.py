'''
write a python program that calcualtes the gross pay of a few employees.
Define a function that performs the calcualtions and prints out.
The main function runs a loop in which the processPays() is called for every employee.
The function has one parameter, employees count thats passed when calling it.
'''

def processPays(hrs,payRate):
    gross = hrs * payRate
    print(f'Your gross pay is: ${gross}')

def main():
    list = []
    empCount = int(input('Enter the number of employees: '))
    count = 0
    while count < empCount:
        hrs , payRate = input('Enter your hours and payrate: ').split()
        hrs , payRate = float(hrs), float(payRate)
        processPays(hrs,payRate)
        count += 1
        list.append(hrs)
        list.append(payRate)
        print(list)

if __name__  == '__main__':
    main()
