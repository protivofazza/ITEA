import models as m
import schemas as s
import random
import crud

SUBJECTS = ('English', 'Ukrainian', 'Physics', 'Biology', 'Chemistry', 'History', 'Calculus AB', 'Trigonometry')

DEPARTMENTS = ('Computer Science', 'Economy', 'Mathematics', 'Business', 'Dancing')

CURATORS = []
with open("curator_names.txt") as file:
    lines = file.readlines()
    for line in lines:
        name, surname = line[:-1].split(' ')
        CURATORS.append({"name": name, "surname": surname})
    CURATORS = tuple(CURATORS)

STUDENTS_NAMES = []
with open("student_names.txt") as file:
    lines = file.readlines()
    for line in lines:
        name, surname = line[:-1].split(' ')
        STUDENTS_NAMES.append({"name": name, "surname": surname})
    STUDENTS_NAMES = tuple(STUDENTS_NAMES)


def add_subjects():
    new = 0
    for subject in SUBJECTS:
        subject = {"name": subject}
        subject_db = m.Subject.objects.filter(**subject)
        if subject_db:
            continue
        new += 1
        print(f"Created subject: {crud.create(m.Subject, s.SubjectSchema, subject)}")
    print(f"Created {new} new subjects")


def add_departments():
    new = 0
    for department in DEPARTMENTS:
        department = {"name": department}
        department_db = m.Department.objects.filter(**department)
        if department_db:
            continue
        new += 1
        print(f"Created department: {crud.create(m.Department, s.DepartmentSchema, department)}")
    print(f"Created {new} new departments")


def add_curators():
    new = 0
    for curator in CURATORS:
        curator_db = m.Curator.objects.filter(**curator)
        if curator_db:
            continue
        new += 1
        print(f"Created curator: {crud.create(m.Curator, s.CuratorSchema,curator)}")
    print(f"Created {new} new curators")


def add_students():
    new = 0
    for student_name in STUDENTS_NAMES:
        student_db = m.Student.objects.filter(**student_name)
        if student_db:
            continue

        student = student_name

        subjects = m.Subject.objects
        grades_count = random.randint(0, 5)
        student['grades'] = []
        for i in range(grades_count):
            subject = str(subjects[random.randint(0, len(subjects) - 1)].id)
            grade = random.randint(0, 100)
            grade = s.GradeSchema().load({"grade": grade, "subject": subject})
            grade = m.Grade.objects.create(**grade).save()
            student['grades'].append(str(grade.id))
        curators = m.Curator.objects
        student['curator'] = str(curators[random.randint(0, len(curators) - 1)].id)

        departments = m.Department.objects
        student['department'] = str(departments[random.randint(0, len(departments) - 1)].id)

        new += 1
        print(f"Created student: {crud.create(m.Student, s.StudentSchema, student)}")
    print(f"Created {new} new students")


if __name__ == '__main__':
    add_subjects()
    add_curators()
    add_departments()
    add_students()
