route, destination = input("enter a distance and price: ").split()
route = int(route)

if route == 1:
    if destination == 'abc':
        ticket = 2.5
    else:
        ticket = 4.75
else:
    ticket = 1.0
print('goodbye')
print(ticket)