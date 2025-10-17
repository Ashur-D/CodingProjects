# slicing a list

sales = ['prod1',23,45.0,'prod2',66,9.9,'prod3',101,56.7]

slice1 = sales[0:3]
print('product1 info:',slice1)

slice2 = sales[3:6]
print('product2 info:',slice2)

slice3 = sales[6:9]
print('product3 info:',slice3)

# since lists are mutable we can assign them 

sales[0] = 'fans'
print(sales[0])
print(sales)

