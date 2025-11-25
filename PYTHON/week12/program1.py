def processSales():
    sales = []
    sales.append(477.1)
    sales.append(447.9)
    sales.append(847.8)
    sales.append(695.2)
    sales.append(597.6)
    sales.append(903.3)
    return sales

def main():
    theSales = processSales()
    total = 0
    for sale in theSales:
        if sale > 500.00 and sale < 700.00:
            total += sale
    print('The total of the sales is',round(total,2))

if __name__ == '__main__':
    main()
