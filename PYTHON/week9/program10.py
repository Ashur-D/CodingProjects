students = {123:'jhon', 506:'salma', 900:'rahul', 782:'lana'}
print(students)

students[666] = 'Nadia' # to append to a dictonary, type the dictonary,followed by key and equaled to item
students[662] = 'adam'
print(students)

st1 = students[900]
print(st1)

students[782] = 'sally'
st2 = students[782]
print(st2)

# attempting to assign a new value to an existing key
students[782] = 'nadia'
print(students)