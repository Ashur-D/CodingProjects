list1 = [111,222,333]
list2 = [3,9,7]
# create a dictionary whose keys are content of list1 and list 2 variales
# whose keys are contnet of list1 and vlaues are content of list2
#
dict1 = {}

for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)

# or

dict1[list1[0]] = list2[0]
dict1[list1[1]] = list2[1]
dict1[list1[2]] = list2[2]

###############################################################################################


# for loop that iterates thru the dictionary and calc the total of quantity
total = 0
for k,v in dict1.items():
    total += v
print(total)

###############################################################################################

total2 = 0
for k,v in dict1.items():
    total2 += k
print(total2)

###############################################################################################


# for the above loop, look up a key, if found print its value; otherwise, print "key not found"

user = int(input('Enter a key value to find: '))

for k,v in dict1.items():
    if user == k:
        print(k)
        break
else:
    print('error')

###############################################################################################

user = int(input('Enter a key value to find: '))

flag = 'y'
user = int(input('Enter a key value to find: '))
while flag.lower() == 'y':
    for k,v in dict1.items():
        if user == k:
            print(k)
            break
    else:
        print('error')
    flag = input('Would you like to keep going?: ').lower()

###############################################################################################

