with open('C:\\Users\\ashur\\Downloads\\outputfile.txt') as outputfile:
    content = outputfile.readline() # reads the next line in the file and returns each line as a string

    line1 = outputfile.readline() # reads the next line in the file and returns the whole content as 1 string
    print(line1,end='') # prints content to the terminal

    line2 = outputfile.readline()
    print(line2,end='')
