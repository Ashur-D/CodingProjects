import random

list1 = [23, 13, 98, -67, -12, 45, 41]
x = random.choice(list1) # returns a random number from list1
print(x)
print(random.shuffle(list1)) # shuffles items in list1,
x = random.shuffle(list1)
print(list1)
print(x)