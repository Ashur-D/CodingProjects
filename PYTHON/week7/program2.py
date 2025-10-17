salary, yox = input("Enter your salary and years of experience: ").split()
salary = int(salary)
yox = int(yox)
bonus = 0

if salary > 60000:
    if yox > 10:
        bonus += 2000
    else:
        bonus += 1000
elif salary < 60000:
    if yox > 20:
        bonus += 800
    else:
        bonus += 0
else:
    bonus = 0
print("your bonus is",bonus)