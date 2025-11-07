# a program that prints out numbers from 1 to 10 but skips number 6 using continue

count = 0

while count < 10:
    count += 1
    if count == 6:
        continue # jump to the top of the loop to line 5
    print('the current number is', count)
print('Thanks!')