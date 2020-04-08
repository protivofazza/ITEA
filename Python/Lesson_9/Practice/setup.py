import models as m
import schemas as s
import crud


department = crud.read(m.Department)[1]
students = m.Student.get_honored_by_department(department)
for student in students:
    print(student.grades)

curator = crud.read(m.Curator)[0]
students = m.Student.get_students_by_curator(curator)
for student in students:
    print(student.curator)
