from abc import ABC, abstractmethod
import datetime


class Person(ABC):

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def get_age_in_years(self):
        pass


class Enrollee(Person):

    def __init__(self, surname, day_birthday, month_birthday, year_birthday, department):
        self._surname = surname
        self._birthday = datetime.datetime(year_birthday, month_birthday, day_birthday)
        self._department = department

    @property
    def surname(self):
        return self._surname

    def print_info(self):
        print(f"Surname: {self._surname} |\tBirthday: {self._birthday.date()} |\tDepartment: {self._department}")

    def get_age_in_years(self):
        return (datetime.datetime.now() - self._birthday).days // 365


class Student(Person):

    def __init__(self, surname, day_birthday, month_birthday, year_birthday, department, course):
        self._surname = surname
        self._birthday = datetime.datetime(year_birthday, month_birthday, day_birthday)
        self._department = department
        self._course = course

    @property
    def surname(self):
        return self._surname

    def print_info(self):
        print(f"Surname: {self._surname} |\tBirthday: {self._birthday.date()}"
              f" |\tDepartment: {self._department} |\tCourse: {self._course}")

    def get_age_in_years(self):
        return (datetime.datetime.now() - self._birthday).days // 365


class Faculty(Person):

    def __init__(self, surname, day_birthday, month_birthday, year_birthday, department, position, experience):
        self._surname = surname
        self._birthday = datetime.datetime(year_birthday, month_birthday, day_birthday)
        self._department = department
        self._position = position
        self._experience = experience

    @property
    def surname(self):
        return self._surname

    def print_info(self):
        print(f"Surname: {self._surname} |\tBirthday: {self._birthday.date()}"
              f" |\tDepartment: {self._department} |\tPosition: {self._position}"
              f" | \tExperience: {self._experience} years")

    def get_age_in_years(self):
        return (datetime.datetime.now() - self._birthday).days // 365


persons_list = [
    Faculty("Tsvil", 12, 12, 2002, "ECON", "TA", 10),
    Student("Garin", 11, 10, 1985, "STAT", 3),
    Enrollee("DiPierro", 6, 3, 1985, "SCG"),
    Student("Alderson", 31, 5, 1993, "CBS", 2),
    Faculty("Moss", 1, 1, 1991, "MATH", "Prof.", 6)
]

for person in persons_list:
    person.print_info()

for person in persons_list:
    if person.get_age_in_years() in range(25, 30):
        print(f"{person.surname}'s age is in the given range")

print("\n" + "*" * 100 + "\n")