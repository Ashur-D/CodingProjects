'''
• Create an app that calculates the total purchase amount based on the type of customer and subtotal amount.
• Make sure to validate the total entered is not less than 0.
    • If the Customer type is R:
        ◦ If the Subtotal is greater than or equal to 250, the Discount percent is 25%.
        ◦ Else If the Subtotal is greater than or equal to 100 and less than 250, the Discount percent is 10%.
        ◦ Otherwise, the Discount percent is 5%.
    • Else If the Customer type is C:
        ◦ If the Subtotal is greater than or equal to 250, the Discount percent is 30%.
        ◦ Else If the Subtotal is less than 250, the Discount percent is 20%.
    • Else, the Discount percent is 0.
• Repeat the process for a number of customers determined by the system user.
• To implement the above requirements, get the inputs in the main function.
- Define a method (calcDiscounts) that takes two parameters (customer type and total value). The method processes the above comparisons and returns the Discount percent. The loop should run in the main function calling (calcDsicounts) the number of times entered by the user.
• In the main(), print out the customer type, the subtotal amount and the discount percent. Make sure to display informative outputs and you have used (% specifier) to format it.
• Make sure to ask the user if they want to run the application again.
'''

def calcDiscounts(customerType,totalValue):
    discount = 0.0
    if customerType == 'R':
        if totalValue >= 250:
            discount = 0.25
        elif totalValue >= 100 and totalValue < 250:
            discount = 0.10
        else:
            discount = 0.05
    elif customerType == 'C':
        if totalValue >= 250:
            discount = 0.30
        elif totalValue < 250:
            discount = 0.20
    else:
        discount = 0
    return discount

def main():
    repeat = 'YES'

    while repeat:
        count = 0
        user = int(input('Enter a number of customers: '))
        while user < 0:
            user = int(input('Please try again: '))

        # for i in range(user)
        while count < user:
            amount = float(input(f'Enter the amount customer {count+1} spent: '))
            if amount < 0:
                amount = float(input(f'Please try again and enter the amount customer{count+1} spent: '))

            customer_type = input(f'Enter the customer type for customer {count+1}: ').upper()
            if customer_type != 'C' and customer_type != 'R':
                customer_type = input(f'Please try again and enter the customer type for customer {count+1}: ').upper()

            customerDiscount = calcDiscounts(customer_type,amount)
            subTotal = amount * customerDiscount
            total = amount - subTotal
            # print(f'Customer {customer_type} your subtotal was {amount}, your new total is {total} after a {customerDiscount * 100} discount')
            print('Customer %s'%(customer_type),'your subtotal was $%.2f'%(amount),'your new total is $%.2f'%(total),'after a %.0f'%(customerDiscount*100),'% discount')
            count += 1

        repeat = input('Would you like to run the application again?: ').upper()
        if repeat != 'YES':
            break

if __name__ == '__main__':
    main()

############################################################################################################
'''
- Write a python program that performs basic statistics on populations of a few cities in Ontario. First, create an empty dictionary then add to it a few pairs of keys, values of cities with their populations. Create a for loop that iterates through the dictionary. You will perform the following over the dictionary: sum up all the populations, find the minimum value, find the maximum value, find the average value.
- Next, save the values of the populations obtained from the dictionary in a list. Add to the list another list that contains the four values calculated above.
- Practice accessing and printing out a few values in the newly created list.
'''
# def populations():
#     population = {}
#     population ['Toronto'] = 5647656
#     population ['Ottawa'] = 1068821
#     population ['Kitchener'] = 522888
#     population ['London'] = 423369
#     population ['Hamilton'] = 729560
#     return population

# def sumPop(population):
#     totalSum = 0
#     for value in population.values():
#         totalSum += value
#     return totalSum

# def minPop(population):
#     return min(population.values())

# def maxPop(population):
#     return max(population.values())

# def avgPop(population):
#     totalSum = 0
#     for value in population.values():
#         totalSum += value
#     avg = totalSum / len(population)
#     return avg

# def main():
#     pop = populations()
#     newList = []
#     newList.extend([sumPop(pop), minPop(pop), maxPop(pop), avgPop(pop)])
#     newList2 = []
#     newList2.append(newList)
#     print(newList2)
#     print(newList2[0][1]) # access the first list in the list, then access the second item in that list

# if __name__ == '__main__':
#     main()

'''
totalSum = sumPop(pop),minPop(pop),maxPop(pop),avgPop(pop) # this turns it into a tuple

can also append to list with > newList += [sumPop(pop), minPop(pop), maxPop(pop), avgPop(pop)]

or

newList.append(sumPop(pop))
newList.append(minPop(pop))
newList.append(maxPop(pop))
newList.append(avgPop(pop))

avg can be done like this:

totalSum = 0
count = 0
for value in population.values():
    totalSum += value
    count += 1
avg = totalSum / count
return avg
'''
