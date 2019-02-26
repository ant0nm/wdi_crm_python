from peewee import SqliteDatabase, Model, CharField, TextField

# create a database that we'll be connecting to
db = SqliteDatabase('crm.db')

class Contact(Model):
    # we do not need to worry about creating an id anymore
    # peewee will take care of creating an id field that automatically increments
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()

    class Meta:
        database = db

    # the only instance method left over from previous design
    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return "{} {}".format(self.first_name, self.last_name)

db.connect()
db.create_tables([Contact])
