# strings are immmutable ( cannot be changed)

name = 'samir'
name = name + ' ' + 'patel'
print(name)

'''
index start a 0 and go up by 1, and -1 from right to left

to get last index from string, 'len - 1'

len counts the number of characters

'''

lastName = 'karim'
print('length of last name = ',len(lastName)) # printing length of string 'karim'

# creating a user name kar2 for karim
userName = lastName[0:3] + '2' # slicing last_name to get kar2 and concatening slice with string 2; sequence of slicing [start:stop:step]
print('user name is', userName)



str1 = 'azsi2lly4dgooxse'
print(str1[2:4] + str1[5:8] + '', str1[10:13] + str1[14:16])

str1 = 'h89ash09f8ur13gh' # index goes up to 15
print(str1[3:6] + str1[10:12])

# homework, print ashur from '90jfurlkidash8jf'

str1 = '90jfurlkidash8jf'
print(str1[10:13] + str1[4:6])


