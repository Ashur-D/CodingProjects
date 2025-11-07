'''
re-write the vowel program using continue, 
let he user attemp the program 5 times, 
if a vowel is found, it prints a message that it is found
'''

vowels = 'aeiouAEIOU'
attempts = 0

while attempts < 5:
    v = input ('enter a vowel: ')
    attempts += 1
    if v in vowels:
        print('It\'s a vowel')
        continue
    print('This is not a vowel.')
print('thanks!')