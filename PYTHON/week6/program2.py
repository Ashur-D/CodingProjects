# write a python program that deterimes the safe zone for people based of temp value,
# prompt the user to enter temp value, to stay in safe zone, temp must be between 20 and 37
# otherwirse it would be dangerous to stay in. sole problem using bth relationonal and logical operators.

temp = int(input("Enter the temp: "))

if temp >= 20 and temp <= 37:
    safeZone = "safe"
else:
    safeZone = "not safe"
print(safeZone)