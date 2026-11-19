# Student Grade Management System

## 📌 Project Overview

The **Student Grade Management System** is a Python-based application designed to manage student academic records, store subject marks, calculate grades, percentages, and GPA.

The system uses SQLite database connectivity to store student information and provides a menu-driven interface for managing academic details.

## 🎯 Objectives

- Maintain student profiles and academic records.
- Add and display student information.
- Store marks across multiple subjects.
- Calculate total marks and percentages.
- Automatically assign letter grades and GPA.
- Store student records using an SQLite database.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Database:** SQLite
- **IDE:** Visual Studio Code
- **Modules:** sqlite3

## 📂 Project Structure

```text
Student_Grade_Management/
│
├── main.py
├── database.py
├── grade_calculator.py
├── report_card.py
├── students.db
│
├── reports/
│
└── README.md
```

## ⚙️ Features

1. **Add Student:** Enter student ID, name, class and subject marks.
2. **Display Students:** View stored student details and marks.
3. **Calculate Results:** Calculate total marks and percentage.
4. **Grade Calculation:** Assign grades based on student performance.
5. **GPA Calculation:** Calculate GPA based on percentage.
6. **Database Management:** Store academic information using SQLite.

## 📚 Subjects

The application currently supports five subjects:

- Python
- Mathematics
- English
- Computer Science
- Database Management

Each subject carries a maximum of 100 marks.

## 📊 Grading System

| Percentage | Grade | GPA |
|---|---|---|
| 90–100 | A+ | 10 |
| 80–89 | A | 9 |
| 70–79 | B | 8 |
| 60–69 | C | 7 |
| 50–59 | D | 6 |
| 40–49 | E | 5 |
| Below 40 | F | 0 |

## 🚀 How to Run the Project

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Open Terminal

Use the following shortcut:

`Ctrl + ``

### Step 4: Run the Application

Execute:

```bash
py main.py
```

### Step 5: Select an Option

The application displays the following menu:

```text
===== STUDENT GRADE MANAGEMENT =====

1. Add Student
2. Display Students
3. Calculate Grade
4. Exit

Enter your choice:
```

Select the required option and follow the instructions.

## 💻 Sample Result

```text
----- STUDENT RESULT -----

Name: Ravi
Total: 454 / 500
Percentage: 90.8%
Grade: A+
GPA: 10
```

## 🔮 Future Enhancements

- Update student information and marks.
- Delete student records.
- Generate individual student report cards.
- Export academic reports to CSV and PDF.
- Calculate class-wide statistics.
- Develop a graphical user interface (GUI).

## 👩‍💻 Conclusion

The Student Grade Management System provides a simple and efficient way to maintain student academic information. This project demonstrates Python programming, database connectivity, functions, conditional statements, and data management.

It can be further enhanced with additional features to create a comprehensive academic management application.