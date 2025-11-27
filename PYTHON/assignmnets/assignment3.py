def calcDiscounts(customerType,totalValue):

    if customerType == 'R':
        if totalValue >= 250:
            discount = 0.25
    elif customerType == 'C':
        if totalValue >= 250:
            discount = 0.30
    else:
        discount = 0



def main():
    user = int(input('Enter a number of customers: '))
    while user < 0:
        user = int(input('Please try again: '))


if __name__ == '__main__':
    main()
