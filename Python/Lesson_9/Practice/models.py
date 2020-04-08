import mongoengine as me

me.connect("Practice9")


class Subject(me.Document):
    name = me.StringField(min_length=1, max_length=128)

    def __str__(self):
        return f"{self.name}"


class Grade(me.Document):
    subject = me.ReferenceField(Subject)
    grade = me.IntField(min_value=0, max_value=100)

    def __str__(self):
        return f"{self.subject}: {self.grade}"


class Curator(me.Document):
    name = me.StringField(min_length=1, max_length=128)
    surname = me.StringField(min_length=1, max_length=128)

    def __str__(self):
        return f"{self.name}, {self.surname}"


class Department(me.Document):
    name = me.StringField(min_length=1, max_length=128)

    def __str__(self):
        return f"{self.name}"


class Student(me.Document):
    name = me.StringField(min_length=1, max_length=128)
    surname = me.StringField(min_length=1, max_length=128)
    grades = me.ListField(me.ReferenceField(Grade))
    curator = me.ReferenceField(Curator)
    department = me.ReferenceField(Department)

    def __str__(self):
        return f"{self.name}, {self.surname}, Dep: {self.department}"

    @classmethod
    def get_honored_by_department(cls, department):
        students = cls.objects.filter(department=department)
        result = []
        for student in students:
            honored = True
            for grade in student.grades:
                if grade.grade < 90:
                    honored = False
                    break
            if honored:
                result.append(student)
        return result

    @classmethod
    def get_students_by_curator(cls, curator):
        return cls.objects.filter(curator=curator)



