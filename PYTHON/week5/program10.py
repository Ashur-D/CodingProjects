grade = int(input("Enter your grade: "))

if grade >= 50:
    print('%s%15s'%("status", "passed"))
    # grade = ('passed')
else:
    print("failed")
    # grade = ('retake')


print('%s%15d' %("status",grade))
print("status%15s" %grade)
print("status" '%15d' %(grade))
print("status" '%15s' %(grade))