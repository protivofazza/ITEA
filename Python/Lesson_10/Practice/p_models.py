import mongoengine as ME


ME.connect("Practice10")


class Tag(ME.Document):
    name = ME.StringField()

    def __str__(self):
        return self.name


class Author(ME.Document):
    name = ME.StringField()
    surname = ME.StringField()
    number_of_publications = ME.IntField(default=0)

    def __str__(self):
        return self.name + ' ' + self.surname


class Publication(ME.Document):
    title = ME.StringField()
    post = ME.StringField()
    date = ME.DateTimeField()
    author = ME.ReferenceField(Author)
    tags = ME.ListField(ME.ReferenceField(Tag))
    seen_by = ME.IntField(default=0)

    def __str__(self):
        return f'{self.title}\n' \
               f'{self.date}\n' \
               f'{self.post}\n' \
               f'{self.tags}' \
               f'{self.post}'

