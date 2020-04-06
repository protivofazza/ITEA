import mongoengine as me

me.connect("Practice_11")


class Person(me.Document):
    name = me.StringField(min_length=1)
    surname = me.StringField(min_length=1)
    phone_number = me.StringField(min_length=13, max_length=13)
    email = me.EmailField()
    address = me.StringField(min_length=1)
    comments = me.StringField(min_length=1)

    def __str__(self):
        return f"{self.name}, {self.surname}\n" \
               f"{self.phone_number}\n" \
               f"{self.email}\n" \
               f"{self.address}\n" \
               f"{self.comments}"
