# Write a python program that determines the discount percentage based on the purchases amount
# The program should calculate the final bill after taxes and discounts
# Last, the program should print the purchase amount, discount amount, tax amount and final bill with(%)
# The program gets the customer code and total purchases from user, all in one statement

code, total = input("Please Enter Customer Code and Total Purchases: ").split()

total = float(total)
taxRate = 0.13

if total >= 500:
    discount = 0.3
elif total >= 300:
    discount = 0.2
elif total >= 100:
    discount = 0.1
else:
    discount = 0

discountAmount = total * discount
totalAfterDiscount = total - discountAmount

taxAmount = totalAfterDiscount * taxRate
finalBill = taxAmount + totalAfterDiscount

print("%-20s%s"%("Customer Code:", code))
print("%-20s%.2f"%("Total:", total))
print("%-20s%.2f"%("Discount Awarded:", discountAmount))
print("%-20s%.2f"%("Total Taxed:", taxAmount))
print("%-20s%.2f"%("Final Bill:", finalBill))