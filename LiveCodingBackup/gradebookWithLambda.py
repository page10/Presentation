from StudentClassDef import Student


def filter(students, predicate, index=0) -> list:
    if index >= len(students):
        return []

    student_found = filter(students, predicate, index + 1)

    current_student = students[index]
    if predicate(current_student):
        student_found.append(current_student)

    return student_found


students = Student.CreateStudent()

# Find students by name
student_named_harry = filter(
    students, lambda student: student.name == 'Harrier Dubois')

# Find students with final score greater than 83
students_with_final_greater_than_83 = filter(
    students, lambda student: student.final > 83)

# Find students with final score greater than midterm
students_with_final_greater_than_midterm = filter(
    students, lambda student: student.final > student.midterm)

# Find students with average homework score greater than 80
students_with_average_homework_greater_than_80 = filter(
    students, lambda student: sum(student.homework) / len(student.homework) > 80)

print(student_named_harry)
print(students_with_final_greater_than_83)
print(students_with_final_greater_than_midterm)
print(students_with_average_homework_greater_than_80)
