'''
a python program that prompts the user to enter a keyword and it searched the file for the entered word
if it is found, the program returns the line that contains it.
'''

keys = input("Enter a keyword: ")

with open('C:\\Users\\ashur\\Downloads\\outputfile2.txt','r') as outputfile:
    for line in outputfile:
        thisLine = line.split() # split makes the line into a list
        if keys in thisLine:
            print(thisLine)
