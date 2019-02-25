class Contact:

    # class variables
    contacts = []
    next_id = 1

    def __init__(self, first_name, last_name, email, note):
        """This method should initialize the contact's attributes"""
        # contact's basic info
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note
        # assign each contact an id
        self.id =  Contact.next_id
        Contact.next_id += 1

    def __str__(self):
        return "Name: {}  Email: {}  Note: {}  ID: {}".format((self.first_name + ' ' + self.last_name), self.email, self.note, self.id)

    @classmethod
    def create(cls, first_name, last_name, email, note):
        """This method should call the initializer,
        store the newly created contact, and then return it
        """
        new_contact = Contact(first_name, last_name, email, note)
        cls.contacts.append(new_contact)
        return new_contact

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        return cls.contacts

    @classmethod
    def find(cls, requested_id):
        """ This method should accept an id as an argument
        and return the contact who has that id
        """
        requested_contact = None
        for contact in cls.contacts:
            if contact.id == requested_id:
                requested_contact = contact
        if requested_contact:
            return requested_contact
        else:
            return "Could not find contact with id of {}.".format(requested_id)

    def update(self, attribute_to_update, new_value):
        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact
        """
        # every object created is stored as a dictionary
        # get the current object's (self) dictionary
        object_dict = self.__dict__
        if attribute_to_update in object_dict.keys():
            object_dict[attribute_to_update] = new_value
        else:
            return "Could not find a '{}' attribute in the selected contact.".format(attribute_to_update)

    @classmethod
    def find_by(cls, attribute_name, attribute_value):
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value
        eg. searching for 'first_name', 'Betty' should return the first contact named Betty
        """
        requested_contact = None
        if len(cls.contacts) == 0:
            return "Your contacts are empty! There's nothing to search!"
        else:
            first_contact = cls.contacts[0]
            contact_attributes = first_contact.__dict__.keys()
            if attribute_name in contact_attributes:
                for contact in cls.contacts:
                    contact_dict = contact.__dict__
                    if (not requested_contact) and (contact_dict[attribute_name] == attribute_value):
                        requested_contact = contact
                if requested_contact:
                    return requested_contact
                else:
                    return "Could not find contact with attribute name '{}' and attribute value {}.".format(attribute_name, attribute_value)
            else:
                return "The attribute name '{}' is not valid!".format(attribute_name)


    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""
        # remove all the stored contacts
        cls.contacts.clear()
        # reset the id to 1
        cls.next_id = 1

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return self.first_name + ' ' + self.last_name


    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """
        if self in Contact.contacts:
            removed_id = self.id
            Contact.contacts.remove(self)
            # move all the ids > deleted contact's id down by 1
            # this ensures that the mapping between order in list and ID is accurate
            # first contact in the list will always have ID = 1, second will always have ID = 2, and so on...
            Contact.next_id -= 1
            for contact in Contact.contacts:
                if contact.id > removed_id:
                    contact.id -= 1
        else:
            return "There is no such contact!"


# Feel free to add other methods here, if you need them.
