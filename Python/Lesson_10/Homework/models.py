import mongoengine as me

me.connect("Lesson10_HW")


class Category(me.Document):
    name = me.StringField(min_length=3)
    parent_category = me.ReferenceField("self")

    def __str__(self):
        return f"{self.name}"


class Goods(me.Document):
    name = me.StringField(min_length=1)
    model = me.StringField(min_length=1)
    available = me.IntField(min_value=0)
    category = me.ReferenceField(Category)
    price = me.IntField(min_value=0)
    seen_by = me.IntField(min_value=0, default=0)

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}$"
