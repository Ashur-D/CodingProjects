def replace_vowel(string):
    newstring = ''
    vowels = ['a','e','i','o','u']
    for n in range(len(string)):
        letter = string[n]
        if letter in vowels:
            letter = letter.upper()
        newstring = newstring + letter
    return newstring

def remove_doubles(string):
    newstring = ''
    for n in range(len(string)):
        if string[n-1] != string[n]:
            newstring = newstring + string[n]
    return newstring
