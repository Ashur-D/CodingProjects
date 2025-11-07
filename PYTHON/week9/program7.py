# working with list methods

sales1 = [345.89, 567.34,607.34, 987.09, 500.99]
print(sales1)


sales2 = [1234.89,2345.66]
print(sales2)

sales1.extend(sales2) # merges the list, still 1 list
print()
print(sales1)

sales1.append(sales2) # adds a list within a list
print()
print(sales1)
print(sales1[6])