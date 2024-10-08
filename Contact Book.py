 #(link unavailable)
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self):
        self.contacts = []


    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone_number}")


    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False

        for contact in self.contacts:
            if search_term.lower() in (contact.name.lower(), contact.phone_number):
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                found = True
                break

        if not found:
            print("Contact not found.")


    def update_contact(self):
        self.view_contacts()
        index = int(input("Enter contact number to update: ")) - 1

        if index < len(self.contacts):
            contact = self.contacts[index]
            print("Enter new details (press Enter to skip):")

            contact.name = input(f"Name ({contact.name}): ") or contact.name
            contact.phone_number = input(f"Phone Number ({contact.phone_number}): ") or contact.phone_number
            contact.email = input(f"Email ({contact.email}): ") or contact.email
            contact.address = input(f"Address ({contact.address}): ") or contact.address

            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")


    def delete_contact(self):
        self.view_contacts()
        index = int(input("Enter contact number to delete: ")) - 1

        if index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



 
