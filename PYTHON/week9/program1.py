# appedning to list's and printing before and after

courses = ['python','java', 'c', 'csharp']
print(courses)

courses.append('c++') # adds c++ to the end of the list
print(courses)

courses.insert(2,'ruby') # adding ruby to the 3rd index 
print(courses)

courses.remove('ruby') # all items shift back one index
print(courses)

x = courses.pop() # remove the last itme and returns it
print(x)
print(courses)

y = courses.remove('csharp')
print(y)
print(courses)

z = courses.pop(0) 
print(z)
print(courses)


print(courses.index('java')) # returns the index of the item
# print(courses.index('php'))
