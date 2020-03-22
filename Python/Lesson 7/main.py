import sqlite3
import sys


def initialize_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    file = open("sqlllines.txt")
    query = ""
    char = "#"
    while char:
        char = file.read(1)
        if char == ";":
            print("QUERY: " + query)
            try:
                cursor.execute(query)
                connection.commit()
            except sqlite3.OperationalError:
                pass
            query = ""
        else:
            query += char
    file.close()
    connection.close()
    sys.exit(0)


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor = conn.cursor()
cursor.execute(
    f"""
    SELECT * FROM employees
    """
)

for data in cursor:
    print(data)
conn.close()
