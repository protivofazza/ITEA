import json


class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age


class PersonEncoder(json.JSONEncoder):

    def default(self, person):
        if isinstance(person, Person):
            return person.__dict__
        else:
            return json.JSONEncoder.default(self, person)



person = Person('Bruce', 'Lee', 100)
print(person.__dict__)

serialized_person = json.dumps(person, cls=PersonEncoder, indent=4)
print(serialized_person)