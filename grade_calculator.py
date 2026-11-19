
def calculate_result(marks):

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
        gpa = 10

    elif percentage >= 80:
        grade = "A"
        gpa = 9

    elif percentage >= 70:
        grade = "B"
        gpa = 8

    elif percentage >= 60:
        grade = "C"
        gpa = 7

    elif percentage >= 50:
        grade = "D"
        gpa = 6

    elif percentage >= 40:
        grade = "E"
        gpa = 5

    else:
        grade = "F"
        gpa = 0

    return total, percentage, grade, gpa
