from contact import Contact

# test out the Contact class
contact1 = Contact.create('Betty', 'Maker', 'bettymakes@gmail.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@gmail.com', 'beep boop')
contact3 = Contact.create('Anton', 'Moiseev', 'anton.mois33v@gmail.com', 'Loves cats')
print("All contacts:")
print(contact1)
print(contact2)
print(contact3)

print()
print("Current number of contacts:")
print(len(Contact.contacts))
print()
print("Contacts ids:")
print(contact1.id)
print(contact2.id)
print(contact3.id)

print()
print("Current list of contacts:")
print(Contact.all())

print()
requested_id = 3
print("Find contact with id of {}:".format(requested_id))
print(Contact.find(requested_id))

print()
print("Successfully updating a contact:")
contact1.update("first_name", "Elizabeth")
print(contact1)

print()
print("Failed attempt to update a contact:")
print(contact1.update("first name", "Bettie"))
print(contact1)

print()
print("Successfully finding a contact by attribute name and value:")
print(Contact.find_by('first_name', 'Elizabeth'))

print()
print("Specifying an invalid attribute name in find_by() method:")
print(Contact.find_by('first name', 'Elizabeth'))

print()
print("Specifying an invalid attribute value in find_by() method:")
print(Contact.find_by('first_name', 'John'))

print()
print("Deleting all contacts:")
Contact.delete_all()
print(Contact.contacts)

print()
print("Adding the 3 contacts back:")
contact1 = Contact.create('Betty', 'Maker', 'bettymakes@gmail.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@gmail.com', 'beep boop')
contact3 = Contact.create('Anton', 'Moiseev', 'anton.mois33v@gmail.com', 'Loves cats')
print(contact1)
print(contact2)
print(contact3)
print(Contact.contacts)

print()
print("Get full name of each contact:")
for contact in Contact.contacts:
    print(contact.full_name())

print()
print("Deleting a contact successfully:")
contact1.delete()
print(Contact.contacts)
for contact in Contact.contacts:
    print(contact)

print()
print("Failing to delete a contact:")
contact4 = Contact('Mia', 'Monteiro', 'mia@gmail.com', 'Loves to cook')
print(contact4.delete())
