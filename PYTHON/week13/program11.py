# reading unit prices from the user, appending them into a list and returnig the list
def read_prices():
    unit_prices = []
    max = 6
    for i in range(0,max):
        prices = float(input('Enter unit prices: '))
        unit_prices.append(prices)
    return unit_prices

def write_prices(unit_prices):
    with open('prices.txt','w') as prices_file:
        for price in unit_prices:
            prices_file.write(f'{price}\n') # converting int into string

def main():
    list1 = read_prices() # calling reading_prices function to get the prices
    write_prices(list1) # calling write_prices to write the list of prics in the list

if '__name__' == '__main__':
    main()
