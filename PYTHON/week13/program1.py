'''
a python program that calculates the sales amount after tax using the total amount and tax rate.
When calling your function, pass the client and their total.
Use atleast 1 default parameter to demostrate your solution
'''

def calcNet(client,total,taxrate = 0.13):
    taxAmount = total * taxrate
    bill = total - taxAmount
    print(f'Bill: ${round(bill,2)}\nTax Rate: {taxrate}\nTax Amount: {round(taxAmount,2)}\nName: {client}')
    # return(bill,taxAmount,taxrate)

def main():
    client, total = input('Enter your name and total amount: ').split()
    total = float(total)
    taxrate = 0.23 # overrides the default parameter in calcNeet
    # bill, taxAmount, taxrate = calcNet(client,total)
    calcNet(client,total,taxrate)



if __name__ == "__main__":
    main()
