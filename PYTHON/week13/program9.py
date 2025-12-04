'''
a python program that reads lines in a file and counts the number of lines.
'''

lineCount = 0
with open('C:\\Users\\ashur\\Downloads\\outputfile2.txt','r') as outputfile:
    for line in outputfile: # we do not call read() becasue for look automatically reads
        lineCount += 1
    print(f'There are {lineCount} lines')
