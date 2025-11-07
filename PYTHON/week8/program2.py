# write a python program that gets the weights of shipments, and calculates the total of the weights and prints out the total. make sure to use a while loop.

count = 0 # initialize a counter at 0
total = 0 # initialize total that holds the total value 
num_ship = int(input("enter the number of shipments: "))

while count < num_ship: # set a condition to control the loop
    weight = int(input("enter the weight of this shipment: "))
    total += weight #total += weight # can also be written as total = total + weight
    print('shipment ' + str(count + 1) + ' has weight of ' + str(weight)) # note-to-self, + can be replaced for commas (expect the count + 1)
    count += 1 # update the value of count  / can also be displayed as count = count + 1
print('The total weights of all your shipments are ', total)
print('the average of all weights is', round(total/count,2))