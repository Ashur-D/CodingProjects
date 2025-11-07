# write a python program that gets the weights of shipments, and calculates the total of the weights and prints out the total. make sure to use a while loop. The program only calculates the avergae of only the shipments with valid weights, greater than 0.

count = 0 # initialize a counter at 0
countGood = 0 # initialize a Goodcounter at 0
total = 0 # initialize total that holds the total value

num_ship = int(input("enter the number of shipments: ")) # get the user input of number of shipments they have

while count < num_ship: # set a condition to control the loop
    weight = int(input("enter the weight of this shipment: ")) # while this condition is true, we ask for user input
    # checking for the good weights
    if weight > 0: # if the weight is a negative we skip the if statement
        total += weight # a running total, which is what the user inputs adding on to the previous (starting from 0)
        print('shipment ' + str(count + 1) + ' has weight of ' + str(weight)) 
        countGood += 1 # update the value of goodCount
    count += 1 # update the number of the general count of shipments
print('The total weights of all your shipments are ', total)
print('the average of all weights is', round(total/count,2))