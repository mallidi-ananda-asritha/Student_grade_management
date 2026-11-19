
import database
import sqlite3
from grade_calculator import calculate_result


def add_student():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    class_name = input("Enter Class: ")

    print("\nEnter marks out of 100")

    python = int(input("Python: "))
    maths = int(input("Maths: "))
    english = int(input("English: "))
    cs = int(input("Computer Science: "))
    db = int(input("Database: "))

    marks = [python, maths, english, cs, db]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Invalid marks! Enter marks between 0 and 100.")
        conn.close()
        return

    try:
        cursor.execute("""
            INSERT INTO students
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (student_id, name, class_name,
              python, maths, english, cs, db))

        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Student ID already exists!")

    finally:
        conn.close()


def display_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    for student in records:
        print(student)

    conn.close()


def calculate_student_grade():

    student_id = int(input("Enter Student ID: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    student = cursor.fetchone()
    conn.close()

    if student:

        marks = list(student[3:8])

        total, percentage, grade, gpa = calculate_result(marks)

        print("\n----- STUDENT RESULT -----")
        print("Name:", student[1])
        print("Total:", total, "/ 500")
        print("Percentage:", percentage, "%")
        print("Grade:", grade)
        print("GPA:", gpa)

    else:
        print("Student not found!")


def main():

    while True:

        print("\n===== STUDENT GRADE MANAGEMENT =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Grade")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            calculate_student_grade()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
