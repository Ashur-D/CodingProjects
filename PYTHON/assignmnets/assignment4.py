import random

def displayMenu():
    print("COMMAND MENU")
    print("Walk - Walk down the path")
    print("Show - Show all items")
    print("Drop - Drop an item")
    print("Exit - Exit program")
    print()

def userInput():
    while True:
        command = input('Command: ').lower()
        if command == 'walk':
            walk()
        elif command == 'show':
            show()
        elif command == 'drop':
            drop()
        else:
            break

def walk():
    with open('C:\\Users\\ashur\\Downloads\\assignment4\\wizard_all_items.txt','r') as outputfile:
        items = outputfile.readlines()
        newItems = []
        for item in items:
            item = item.replace('\n', '')
            newItems.append(item)
        randomItem = random.choice(newItems)
        print(f'f while walking down a path, you see {randomItem}\n would you like to pick it up? (y/n)')


def show():
  with open('C:\\Users\\ashur\\Downloads\\assignment4\\named_wizard_inventory.txt','r') as outputfile:
      print(outputfile)


def drop():
    print('hi')



def main():
    displayMenu()
    userInput()


if __name__ == '__main__':
    main()
