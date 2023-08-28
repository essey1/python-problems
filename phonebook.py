# Create a simple dictionary-based phonebook program.

phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print("Contact added successfully!")

def search_contact(name):
    if name in phonebook:
        print(name + "'s Phone number:" + phonebook[name])
    else:
        print("Contact not found.")

def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(name + "'s Contact removed successfully!")
    else:
        print("Contact not found.")

def display_contacts():
    if phonebook:
        print("Phonebook contacts:")
        for name, number in phonebook.items():
            print(name + ": " + number)
    else:
        print("Phonebook is empty.")

# Usage
add_contact("Abel", "0987654321")
add_contact("Ali", "0912345678")
add_contact("Berhe", "0912332113")
search_contact("Abel")
remove_contact("Berhe")
display_contacts()