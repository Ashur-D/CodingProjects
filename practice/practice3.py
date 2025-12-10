def add_manager_contact(contact_list):
    """
    Takes a list of lists, asks user for new info,
    appends the new list, and returns the modified list.
    """
    print("--- Enter New Contact Information ---")

    # 1. Ask the user for the new details
    new_name = input("Enter Name: ")
    new_phone = input("Enter Phone: ")
    new_email = input("Enter Email: ")

    # 2. Create a new list for this specific person
    new_contact = [new_name, new_phone, new_email]

    # 3. Append this new list to the main list
    contact_list.append(new_contact)

    # 4. Return the updated main list
    return contact_list

def main():
    # 1. Create the initial list of two lists
    managers = [
        ['Karim', '416 123 4567', 'karim@abc.com'],
        ['Lilly', '416 567 4321', 'lilly@abc.com']
    ]

    # 2. Call the function to add a new contact
    updated_managers = add_manager_contact(managers)

    # 3. Print the final result
    print("\nUpdated List of Managers:")
    print(updated_managers)

if __name__ == "__main__":
    main()
