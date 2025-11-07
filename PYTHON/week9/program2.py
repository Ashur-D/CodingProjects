# working with random
import random

# print(random.random()) # retruns a value 0 to 1
count = 0
while count < 10:
    x = random.random()
    # print(x * 10)
    print(int(x * 10))
    count += 1