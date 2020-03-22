import sqlite3


DATABASE = "database.db"
STUDENTS_TABLE_SIGNATURE = ('id', 'name', 'surname', 'department_id', 'group_id', 'identifier')


class DataBaseConnect:

    def __init__(self, database_name):
        self._db = database_name
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._db)
        return self._conn

    def __exit__(self, *args):
        self._conn.close()



def read_query(query="", *args):
    with DataBaseConnect(DATABASE) as connection:
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute(query, list(args))
            result = cursor.fetchall()
        except Exception as e:
            print("An error occured while querying: " + query)
            print(e)
        finally:
            return result


def update_query(query="", *args):
    with DataBaseConnect(DATABASE) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, list(args))
            connection.commit()
        except Exception as e:
            print("An error occured while querying: " + query)
            print(e)


def print_student_grades(student_id):
    grades = read_query("""
                            SELECT g.grade, s.name
                            FROM grades g
                            INNER JOIN subjects s on g.subject_id = s.id
                            WHERE g.student_id = ?""",
                        student_id)
    if grades:
        print(f"Grades:")
        for grade in grades:
            print(f"   {grade[1]} - {grade[0]}")
    else:
        print("No grades are available for this student.")



def print_student_info_with_grades(student_id):
    student = read_query("""
                        SELECT stud.id, stud.name, stud.surname, d.name, g.name, stud.identifier
                        FROM students stud
                        INNER JOIN departments d on stud.department_id = d.id
                        INNER JOIN groups g on stud.group_id = g.id
                        WHERE stud.id = ?""",
                         student_id)
    if student:
        print("--------------------------------------------------------------------------")
        student = student[0]
        print(f"Id: {student[0]}\n"
              f"Name: {student[1]}, {student[2]}\n"
              f"Department: {student[3]}\n"
              f"Group: {student[4]}\n"
              f"Student identifier: {student[5]}")
        print_student_grades(student[0])
        print("--------------------------------------------------------------------------")
    else:
        print(f"Student with id '{student_id}' not found.")


while True:
    n = input("0: Exit; 1 - Login:\n")
    try:
        n = int(n)
    except ValueError:
        continue
    if n == 0:
        break
    elif n == 1:
        login = input("Login: ")
        password = input("Password: ")
        user = read_query("SELECT * FROM users WHERE login = ? and password = ?", login, password)
        if not user:
            print("Invalid login or/and password")
            continue
        user = user[0]
        while True:
            n = input("0: Logout; 1: Get honored students; 2: Get all students; 3: Find by identifier; "
                      "4: Find by id; 5: Add a student; 6: Change a student; 7: Add grade(s) for a student:\n")
            try:
                n = int(n)
            except ValueError:
                continue
            if n == 0:
                break
            elif n == 1:
                honored_students_ids = read_query("""
                                                SELECT s.id FROM students s, grades g
                                                WHERE s.id = g.student_id and s.id not in (
                                                    SELECT s.id FROM students s, grades g
                                                    WHERE s.id = g.student_id and g.grade < 90
                                                    )
                                                GROUP BY s.id
                                                ORDER BY s.id
                                                """)
                for honored_student_id in honored_students_ids:
                    print_student_info_with_grades(honored_student_id[0])
            elif n == 2:
                students_ids = read_query("SELECT id FROM students ORDER BY id")
                for student_id in students_ids:
                    print_student_info_with_grades(student_id[0])
            elif n == 3:
                identifier = input("Enter the identifier's code: ")
                student_id = read_query("SELECT id FROM students "
                                        "WHERE identifier = ?",
                                        identifier)
                student_id = student_id[0]
                if student_id:
                    print_student_info_with_grades(student_id[0])
                else:
                    print(f"No student with the identifier '{identifier}' found.")
            elif n == 4:
                id_ = input("Enter student's id: ")
                print_student_info_with_grades(id_)
            elif 5 <= n <= 7:
                if user[-1]:  # if admin
                    if n == 5:
                        departments = read_query("SELECT * FROM departments")
                        groups = read_query("SELECT * FROM groups")

                        print("Adding a student")
                        name = input("   Name: ")
                        surname = input("   Surname: ")

                        print("   Departments: ")
                        for d in departments:
                            print(f"      {d[0]} - {d[1]}")
                        while True:
                            department = input("   Select department: ")
                            try:
                                department = int(department)
                                break
                            except ValueError:
                                print(f"Field 'Department' must be an integer")

                        print("Groups: ")
                        for g in groups:
                            print(f"      {g[0]} - {g[1]}")
                        while True:
                            group = input("   Select a group: ")
                            try:
                                group = int(group)
                                break
                            except ValueError:
                                print("Field 'Group' must be an integer")

                        while True:
                            identifier = input("Enter the number of student's identifier: ")
                            if identifier[:2].isalpha() and identifier[2:].isdigit() and len(identifier) == 9:
                                break
                            else:
                                print("Incorrect identifier. Identifier must be in format 'AB0123456")
                        save_info = input("Save Info? 0 - No; 1 - Yes: ")
                        if save_info:
                            update_query("""
                                        INSERT INTO students (name, surname, department_id, group_id, identifier)
                                        VALUES (?, ?, ?, ?, ?)
                                        """,
                                         name, surname, department, group, identifier)
                    elif n == 6:
                        student_id = input("Enter the id of the student you want to change info about: ")
                        student = read_query("SELECT * FROM students WHERE id = ?", student_id)
                        if not student:
                            print("The student with this id does not exist")
                            continue
                        while True:
                            print_student_info_with_grades(student_id)
                            print("What do you want to change? (enter 0 to exit):\n"
                                  "   1 - Name\n"
                                  "   2 - Surname\n"
                                  "   3 - Department\n"
                                  "   4 - Group\n"
                                  "   5 - Identifier")
                            code = input()
                            try:
                                code = int(code)
                            except ValueError:
                                continue
                            value = None
                            if code == 0:
                                break
                            elif code == 1:
                                value = input("New name: ")
                            elif code == 2:
                                value = input("New surname: ")
                            elif code == 3:
                                departments = read_query("SELECT * FROM departments")
                                print("Departments: ")
                                for d in departments:
                                    print(f"   {d[0]} - {d[1]}")
                                while True:
                                    value = input("Select new department: ")
                                    try:
                                        value = int(value)
                                        break
                                    except ValueError:
                                        print(f"Field 'Department' must be an integer")
                            elif code == 4:
                                groups = read_query("SELECT * FROM groups")
                                print("Groups: ")
                                for g in groups:
                                    print(f"   {g[0]} - {g[1]}")
                                while True:
                                    value = input("Select new group: ")
                                    try:
                                        value = int(value)
                                        break
                                    except ValueError:
                                        print("Field 'Group' must be an integer")
                            elif code == 5:
                                while True:
                                    value = input("Enter the number of student's identifier: ")
                                    if value[:2].isalpha() and value[2:].isdigit() and len(value) == 9:
                                        break
                                    else:
                                        print("Incorrect identifier. Identifier must be in format 'AB0123456")
                            save_info = input("Save Info? 0 - No; 1 - Yes: ")
                            if save_info:
                                update_query("""
                                            UPDATE students
                                            SET """ + STUDENTS_TABLE_SIGNATURE[code] + """ = ?
                                            WHERE id = ?
                                            """,
                                             value, student_id)
                    elif n == 7:
                        while True:
                            student_id = input("Enter student's id to add grade(s): ")
                            try:
                                student_id = int(student_id)
                                break
                            except ValueError:
                                print("Field 'id' must be an integer")
                        while True:
                            print(f"Current grades for student with id {student_id}:")
                            print_student_grades(student_id)
                            subjects = read_query("SELECT * FROM subjects")
                            for subject in subjects:
                                print(f"{subject[0]} - {subject[1]}")
                            while True:
                                subject_id = input("Please choose the subject: ")
                                try:
                                    subject_id = int(subject_id)
                                    if not read_query("SELECT id FROM subjects WHERE id = ?", subject_id):
                                        raise ValueError
                                    break
                                except ValueError:
                                    print("Field 'id' must be an integer and in the given range")
                            while True:
                                grade = input("Enter the grade (0-100): ")
                                try:
                                    grade = int(grade)
                                    if not 0 <= grade <= 100:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print("Field 'grade' must be an integer in the range [0-100]")
                            save_info = input("Save Info? 0 - No; 1 - Yes: ")
                            if save_info:
                                update_query("INSERT INTO grades (grade, subject_id, student_id) VALUES (?, ?, ?)",
                                             grade, subject_id, student_id)
                            while True:
                                continue_ = input("Add one more grade for this student? 0 - No; 1 - Yes: ")
                                try:
                                    continue_ = int(continue_)
                                    if not 0 <= continue_ <= 1:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print("Field 'code' must be an integer in the range [0-1]")

                            if not continue_:
                                break

                else:
                    print("Forbidden: You must be an administrator to be allowed to use this commands.")
                    continue
            else:
                continue
    else:
        continue
