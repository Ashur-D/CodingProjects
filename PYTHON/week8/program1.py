# write a python program that gets the weights of shipments, prints the out the weights then prints put the number of shipments

count = 0 # initialize a counter at 0

num_ship = int(input("enter the number of shipments: "))

while count < num_ship: # set a condition to control the loop
    weight = int(input("enter the weight of this shipment: "))
    print('shipment ' + str(count + 1) + ' has weight of ' + str(weight))
    count += 1 # update the value of count  / can also be displayed as count = count + 1
print('Thanks!')

