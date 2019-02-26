from contact import Contact

class CRM:

    def main_menu(self):
        while True:
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print()
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ', end="")

    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()
        elif user_selected == 6:
            exit()
        else:
            print("Please enter a valid number: 1 to 6.")

    def add_new_contact(self):
        # get all the required info from our user:
        print('Enter First Name: ', end="")
        first_name = input()

        print('Enter Last Name: ', end="")
        last_name = input()

        print('Enter Email Address: ', end="")
        email = input()

        print('Enter a Note: ', end="")
        note = input()

        contact = Contact.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            note = note
        )


    def modify_existing_contact(self):
        print("Enter the ID of the contact you're looking for: ", end="")
        entered_id = int(input())

        print("Which attribute do you want to modify?")
        print("* first_name")
        print("* last_name")
        print("* email")
        print("* note")
        print("Enter an attribute from the list above: ", end="")
        entered_attribute = input()

        print("Enter a new value for the selected attribute: ", end="")
        entered_value = input()

        selected_contact = Contact.find(entered_id)

        if isinstance(selected_contact, str):
            print(selected_contact)
        else:
            response = selected_contact.update(entered_attribute, entered_value)
            if isinstance(response, str):
                print(response)
            else:
                print("The selected contact has been modified to:")
                print(selected_contact)

    def delete_contact(self):
        print("Enter the ID of the contact you wish to delete: ", end="")
        entered_id = int(input())

        selected_contact = Contact.find(entered_id)

        if isinstance(selected_contact, str):
            print(selected_contact)
        else:
            selected_contact.delete()
            print("Contact has been successfully deleted.")

    def display_all_contacts(self):
        if len(Contact.contacts) == 0:
            print("You have no contacts yet. There is nothing to display!")
        else:
            print("List of all your current contacts:")
            for contact in Contact.contacts:
                print("*", contact.full_name())

    def search_by_attribute(self):
        print("Which attribute do you want to search by?")
        print("* first_name")
        print("* last_name")
        print("* email")
        print("* note")
        print("Enter an attribute from the list above: ", end="")
        entered_attribute = input()

        print("Enter your search term: ", end="")
        entered_value = input()

        response = Contact.find_by(entered_attribute, entered_value)

        if not isinstance(response, str):
            print("The FIRST contact to match your search criteria:")

        print(response)

# create a customer relationship manager
# open the main menu
a_crm_app = CRM()
a_crm_app.main_menu()
