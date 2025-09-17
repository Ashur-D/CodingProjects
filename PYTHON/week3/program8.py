# 9/17/2025

"""
Write a python program that calcualtes the
average of the 3 sales amounts of a store.
"""

store_loc = input("enter the store location: ")

# we cast (do conversion) the user inpts as strings into float numbers.
sales1 = float(input("Enter the first amount of sales:"))
sales2 = float(input("Enter the second amount of sales:"))
sales3 = float(input("Enter the third amount of sales:"))

avg = (sales1 + sales2 + sales3) / 3
print("The store in", store_loc, "had an average sales of", round(avg, 2) ) 
