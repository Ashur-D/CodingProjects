with open('C:\\Users\\ashur\\Downloads\\outputfile.txt') as outputfile:
    content = outputfile.read() # reads the entier file as a string
    print(content) # prints the content to the termianl
    print(content[6:19])
