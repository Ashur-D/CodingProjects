with open('C:\\Users\\ashur\\Downloads\\outputfile.txt') as outputfile:
    content = outputfile.readlines() # reads the entire file as a list
    print(content[0], end='') # prints content to the terminal
    print(content[1])
    print()
