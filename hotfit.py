import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'])

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Contact.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the contact file.")
        return []

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)

def add_contact(contacts, name, phone, email):
    contacts.append(Contact(name, phone, email))

def list_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def delete_contact(contacts, name):
    contacts[:] = [contact for contact in contacts if contact.name != name]

def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)
    
    while True:
        print("\n1. Add Contact")
        print("2. List Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
