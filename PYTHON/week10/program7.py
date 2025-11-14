# a program that searches a code in a dict, if found it returns its value, otherwise it prints a message 'server is not found' To solve it use a for loop, break and else
# ask the user if they need to keep trying the app, and stop whenever they need

myDict1 = {}
myDict1 ['ibm'] = '12345'
myDict1 ['ibm-x'] = '1245-x'
myDict1 ['hp'] = '45678'
myDict1 ['asus'] = '56901'
myDict1 ['lenovo'] = '123456'

yes = 'yes'
while yes.lower() == 'yes' or yes.lower() == 'y':
    search = input('Enter the server code: ')
    for server, code in myDict1.items():
        if code == search:
            print('%10s%10s'%(server,code))
            break
    else:
        print('Server does not exist')
    yes = input('Would you like to try again?(y/n)').lower()
print('thanks')
