scores1 = [55, 80, 92, 45, 78, 88, 60]

failed = 0
passedList = []

for i in scores1:
    if i > 60:
        passedList.append(i)
    else:
        failed += 1
print(passedList)
