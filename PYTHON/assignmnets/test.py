vehicle_num = []
miles_list = []
gallons_list = []
mpg_list = []

num_vehicles = int(input("Enter the number of vehicles: "))

counter = 0
while counter < num_vehicles:
    print('\nVehicle #'+str(counter+1))

    miles = 0
    while miles <= 0:
        miles = float(input("Enter miles driven: "))
        if miles <= 0:
            print("Miles must be a positive number. Try again.")

    gallons = 0
    while gallons <= 0:
        gallons = float(input("Enter gallons used: "))
        if gallons <= 0:
            print("Gallons must be a positive number. Try again.")

    mpg = miles / gallons

    vehicle_num.append(counter + 1)
    miles_list.append(miles)
    gallons_list.append(gallons)
    mpg_list.append(mpg)

    counter += 1


print("\n%-3s\t%-10s\t%-10s\t%-10s" % ("v#", "miles", "gallons", "mpg"))
print("***\t**********\t**********\t**********")

counter2 = 0
while counter2 < num_vehicles:
    print("%-3d\t%-10.1f\t%-10.1f\t%-10.2f" %
          (vehicle_num[counter2], miles_list[counter2], gallons_list[counter2], mpg_list[counter2]))
    counter2 += 1
