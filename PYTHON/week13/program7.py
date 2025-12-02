'''
reading items from a list and writing them into a file
'''

servers = ['ibm-56','cisco-39','lenevo-z','asus-x3','hp-b9','cisco-m56']

with open('C:\\Users\\ashur\\Downloads\\outputfile2.txt','w') as outputfile:
    for i in servers:
        outputfile.write(f'{i}\n')
