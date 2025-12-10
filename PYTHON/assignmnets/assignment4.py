import random

def displayMenu():
    print("COMMAND MENU")
    print("Walk - Walk down the path")
    print("Show - Show all items")
    print("Drop - Drop an item")
    print("Exit - Exit program")

def userInput(owned_items,all_items):
    while True:
        command = input('\nCommand: ').lower()
        if command == 'walk':
            walk(owned_items,all_items)
        elif command == 'show':
            show(owned_items)
        elif command == 'drop':
            drop(owned_items,all_items)
        else:
            print('bye!')
            break

def walk(owned_items,all_items):

    randomItem = random.choice(all_items)
    ans = input(f'While walking down a path, you see {randomItem}\nwould you like to pick it up? (y/n): ')
    if ans == 'y':
        if randomItem in owned_items:
            print(f'Sorry you already have {randomItem}')
        elif len(owned_items) >= 4:
            print('Sorry you cannot have more than 4 items')
        else:
            print(f'you picked up {randomItem}')
            owned_items.append(randomItem)
            all_items.remove(randomItem)
            with open('C:\\Users\\Ash\\Downloads\\assignment4\\wizard_all_items.txt','w') as items_file:
                for item in all_items:
                    items_file.write(str(item) + '\n')
            with open('C:\\Users\\Ash\\Downloads\\assignment4\\named_wizard_inventory.txt','a') as inventory_file:
                    inventory_file.write('\n' + str(randomItem))

def show(owned_items):
    if len(owned_items) == 0:
        print('No items to show')
    else:
        count = 1
        for item in owned_items:
            print(f"{count}. {item}")
            count += 1

def drop(owned_items,all_items):
    ans = int(input('Number: '))
    if ans >= 1 and ans <= len(owned_items):
        removed_item = owned_items.pop(ans - 1)
        all_items.append(removed_item)
        print(f"Dropped {removed_item}.")

        with open('C:\\Users\\Ash\\Downloads\\assignment4\\named_wizard_inventory.txt','w') as inventory_file:
            for item in owned_items:
                inventory_file.write(item + '\n')

        with open(r'C:\Users\Ash\Downloads\assignment4\wizard_all_items.txt','w') as items_file:
            for item in all_items:
                items_file.write(str(item) + '\n')
    else:
        print('invalid number or no items left to drop.')


def ownItems(owned_items):
    with open('C:\\Users\\Ash\\Downloads\\assignment4\\named_wizard_inventory.txt','r') as inventory_file:
        items = inventory_file.readlines()
        for item in items:
            item = item.replace('\n', '')
            owned_items.append(item)


def loadAllItems(all_items):
        with open('C:\\Users\\Ash\\Downloads\\assignment4\\wizard_all_items.txt','r') as items_file:
            items = items_file.readlines()
            for item in items:
                item = item.replace('\n', '')
                all_items.append(item)

def main():
    owned_items = []
    ownItems(owned_items)

    all_items = []
    loadAllItems(all_items)

    displayMenu()
    userInput(owned_items,all_items)


if __name__ == '__main__':
    main()

'''
originally had loadAllItems and ownItems in the walk function but the function started becoming too big and I started running into problems,
so I made them into seperate functions. Also made sure that those 2 functions run first so that the lists can be created and passed to the rest
of the functions.

'''
