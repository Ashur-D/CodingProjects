'''
write a python program that checks for a letter in a word.
If it exists, the program prints its index. If it does not exist in the word
the program prints 'the letter is not found'
prompt the user to enter both the word and the letter.
Use a for loop to solve it.
'''

word , letter = input('Enter your word and letter you search:  ').split()
flag = False
for w in word:
    if letter == w:
        flag = True
        print('The index of ' + letter + ' is ' + str(word.index(w)))
        break

if flag:
    print('thanks')
else:
    print('The letter is not found')
