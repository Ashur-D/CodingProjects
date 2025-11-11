# write a python program that counts the occurances of a letter in a word (its frequency)
# Use a for loop, if structure and continue


word , letter = input('Enter your word and the letter you search: ').split()
count = 0 # frequency

for w in word:
    if w.upper != letter.upper:
        continue
    else:
        count += 1
print('the count of ' + letter + ' is ' + str(count))
