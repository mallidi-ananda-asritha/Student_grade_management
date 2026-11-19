
import sqlite3

def connect_db():
    return sqlite3.connect("students.db")


def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            class_name TEXT NOT NULL,
            python INTEGER,
            maths INTEGER,
            english INTEGER,
            computer_science INTEGER,
            database INTEGER
        )
    """)

    conn.commit()
    conn.close()

    print("Database table created successfully!")


create_table()
