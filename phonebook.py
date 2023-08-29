# Create a simple dictionary-based phonebook program.

phonebook = {}

def instructions():
    print("Welcome to your Phonebook!")
    print("Enter 'add' to add contact")
    print("Enter 'search' to search for a contact name")
    print("Enter 'remove' to remove contact")
    print("Enter 'display' to display contacts")
    print("Enter 'quit' to exit the program")
instructions()

def add_contact(name, number):
    phonebook[name] = number
    print("Contact added successfully!")

def search_contact(name):
    if name in phonebook:
        print("Name:", name, "\nPhone number:", phonebook[name])
    else:
        print("Contact not found.")

def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(name + "'s Contact has been removed successfully!")
    else:
        print("Contact not found.")

def display_contacts():
    if phonebook:
        print("Phonebook contacts:")
        for name, number in phonebook.items():
            print(name + ": ", number)
    else:
        print("Phonebook is empty.")
        

while True:
    instruction = input("What do you want to do: ").lower()
    
    if instruction == 'add':
        add_contact(input("Name: ").capitalize(), int(input("Number: ")))
    elif instruction == 'search':
        search_contact(input("Name: ").capitalize())
    elif instruction == 'remove':
        remove_contact(input("Name: ").capitalize())   
    elif instruction == 'display':
        display_contacts()
    elif instruction == 'quit':
        print("Exited the phonebook program successfully.")
        break
    else:
        print("Invalid entry. Please try again.")