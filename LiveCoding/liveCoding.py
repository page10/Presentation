from StudentClassDef import Student
students = Student.CreateStudent()

# find students with name.(all students named harrier dubois)
# def find_students_by_name(students, required_name):
#     student_list = []
#     for student in students:
#         if student.name == required_name:
#             student_list.append(student)
#     return student_list


# def check_student_name(required_name):
#     def check_name(student):
#         return student.name == required_name
#     return check_name


def filter(student, predicate, index=0):
    if index >= len(student):
        return []
    student_found = filter(student, predicate, index + 1)
    current_student = student[index]
    if predicate(current_student):
        student_found.append(current_student)

    return student_found


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
