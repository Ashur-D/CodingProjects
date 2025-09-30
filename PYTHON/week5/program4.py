# formatting outputs using % operator

first, last = input("Enter your first and last name: " ).split()
print('%s%s'%(first,last)) # using double %s because we have 2 strings to format
print('%s%s%s'%(first,last,"hello"))
print('%s%15s'%(first,last))


first = "ashur"
last = "dawod"
print('%s'%first)
print('%s'%last)
print()
print('%15s'%first) # postive 15 space to right
print('%-15s'%last) # negative 15 spaces to left

print('%s%15s'%(first,last))