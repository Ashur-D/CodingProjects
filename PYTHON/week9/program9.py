# working with tuples

tuple1 = (58, -9, 10, 109, -34)
print(tuple1)

x,y,z,w,p = tuple1 # unpacking tuple1, assigning each variable to the coresponding value in the tuple1
print('second item in tuple1: ', y)
print(tuple1[:3]) # slicing the tuple

v1 = tuple1[4] # get the 4th index of tuple 1 
print('last item:',v1)

v2 = str(v1) + 'hi' # concatenate v1 and a string
print(v2)

v3 = v1 + w
print(v3)
