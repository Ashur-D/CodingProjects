'''
write a python program that
demostrated using spe and end functions
with the print
'''
'''
Print can take other arguments like (sep) and (end).
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.
'''

# Initialization is when you assign an intial value to a variable, then diffreent values are assigned later in the program.


print("Job title", "professor", sep="|")
print("School name", "FAST", sep=":")
print("Welcome to the school of FAST", end="*******") # adding something between the end strings removes the new line
print( "read", "karim", sep="") # by default sep will remove space
print( "read", "karim", end="\n")
print(456,900,10875, sep='#')