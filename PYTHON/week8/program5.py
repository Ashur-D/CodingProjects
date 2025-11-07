vowels = 'aeiouAEIOU'

while True: # set the condition to True so it always runs
    v = input('Enter a vowel: ')
    if v in vowels:
        print('It\'s a vowel,')
        break # break the loop when a vowel is
    print('This is not a vowel, try again.')
    #print()
print('Thanks')