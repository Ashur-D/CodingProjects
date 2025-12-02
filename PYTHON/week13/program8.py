# reading a file content and saving lines as items in a list
servers = []

with open('C:\\Users\\ashur\\Downloads\\outputfile2.txt','r') as outputfile:
    for line in outputfile:
        line = line.replace('\n', '') # replacing the new lines with an empty line
        servers.append(line)
print(servers)
