# working with lists

sales = ['prod1',23,45.0,'prod2',66,9.9,'prod3',101,56.7]
p1_name = sales[0]
p1_quanity = sales[1]
p1_price = sales[2]
print('product1 name: ',p1_name)
print('product1 quantity: ',p1_quanity) 
print('product1 price: ',p1_price)
sales[1] = str(sales[1])
print(p1_name + sales[1])
