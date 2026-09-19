import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    course TEXT,
    mark INTEGER
)
""")

cursor.execute("""
INSERT INTO students (student, course, mark)
VALUES (?, ?, ?)
""", ("John", "Computer Science", 85))

connection.commit()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(student)

connection.close()
