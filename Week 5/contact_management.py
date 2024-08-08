# contact_management.py

import pickle

# Function to read contacts from a text file
def read_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                contacts.append(line.strip())
    except FileNotFoundError:
        print(f"{filename} not found. Creating a new file.")
    return contacts

# Function to write contacts to a text file
def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

# Function to read contacts from a binary file
def load_contacts_binary(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"{filename} not found. Creating a new file.")
        return []
    except EOFError:
        print("File is empty or corrupted.")
        return []

# Function to write contacts to a binary file
def save_contacts_binary(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

# Function to infer file type based on the extension
def infer_file_type(filename):
    if filename.endswith('.txt'):
        return 'text'
    elif filename.endswith('.dat'):
        return 'binary'
    else:
        raise ValueError("Unsupported file type. Use a '.txt' or '.dat' file.")

# Function to add a contact to a file (infers file type)
def add_contact(filename, contact):
    file_type = infer_file_type(filename)
    if file_type == 'text':
        contacts = read_contacts(filename)
        contacts.append(contact)
        write_contacts(filename, contacts)
    elif file_type == 'binary':
        contacts = load_contacts_binary(filename)
        contacts.append(contact)
        save_contacts_binary(filename, contacts)

# Function to remove a contact from a file (infers file type)
def remove_contact(filename, contact):
    file_type = infer_file_type(filename)
    if file_type == 'text':
        contacts = read_contacts(filename)
        if contact in contacts:
            contacts.remove(contact)
            write_contacts(filename, contacts)
        else:
            print(f"Contact '{contact}' not found.")
    elif file_type == 'binary':
        contacts = load_contacts_binary(filename)
        if contact in contacts:
            contacts.remove(contact)
            save_contacts_binary(filename, contacts)
        else:
            print(f"Contact '{contact}' not found.")

# Function to display all contacts from a file (infers file type)
def display_contacts(filename):
    file_type = infer_file_type(filename)
    if file_type == 'text':
        contacts = read_contacts(filename)
    elif file_type == 'binary':
        contacts = load_contacts_binary(filename)
    print("Contacts:")
    for contact in contacts:
        print(contact)

# User interaction function
def user_interaction():
    while True:
        print("\nContact Management System")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            filename = input("Enter filename (e.g., contacts.txt or contacts.dat): ")
            display_contacts(filename)
        elif choice == '2':
            filename = input("Enter filename (e.g., contacts.txt or contacts.dat): ")
            contact = input("Enter contact name: ")
            add_contact(filename, contact)
        elif choice == '3':
            filename = input("Enter filename (e.g., contacts.txt or contacts.dat): ")
            contact = input("Enter contact name to remove: ")
            remove_contact(filename, contact)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the user interaction function
if __name__ == "__main__":
    user_interaction()
