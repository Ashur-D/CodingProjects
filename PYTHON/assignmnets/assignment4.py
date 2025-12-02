def displayTitle():



def displayMenu():
    print("COMMAND MENU")
    print("Walk - Walk down the path")
    print("Show - Show all items")
    print("Drop - Drop an item")
    print("Exit - Exit program")
    print()


def main():
    displayTitle()
    displayMenu()

    inventory = read_inventory()
    while True:
        command = input('Command: ').lower()
        if command == 'walk':
            walk(inventory)
        elif command == 'Show'
            show(inventory)
        elif command == 'drop':
            drop(inventory)
        elif command == 'exit':
            break
        else:
            print('Not a valid command, please try again. \n')
    print('bye!')


if __name__ == '__main__':
    main()
