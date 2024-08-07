class Phonebook:
    def __init__(self, filename='phonebook.txt'):
        self.filename = filename
        self.phonebook = self.load_phonebook()

    def load_phonebook(self):
        phonebook = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split(',')
                    phonebook[name] = phone_number
        except FileNotFoundError:
            pass
        return phonebook

    def save_phonebook(self):
        with open(self.filename, 'w') as file:
            for name, phone_number in self.phonebook.items():
                file.write(f"{name},{phone_number}\n")

    def add_contact(self, name, phone_number):
        self.phonebook[name] = phone_number
        self.save_phonebook()
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.phonebook:
            print("Phonebook is empty.")
        else:
            for name, phone_number in self.phonebook.items():
                print(f"Name: {name}, Phone Number: {phone_number}")

    def search_contact(self, name):
        if name in self.phonebook:
            print(f"Name: {name}, Phone Number: {self.phonebook[name]}")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.phonebook:
            del self.phonebook[name]
            self.save_phonebook()
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

def main():
    phonebook = Phonebook()

    while True:
        print("\nPhonebook Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            phonebook.add_contact(name, phone_number)
        elif choice == '2':
            phonebook.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            phonebook.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            phonebook.delete_contact(name)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
