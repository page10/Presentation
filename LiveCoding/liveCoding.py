from StudentClassDef import Student
students = Student.CreateStudent()

# find students with name.(all students named harrier dubois)
# def find_students_by_name(students, required_name):
#     student_list = []
#     for student in students:
#         if student.name == required_name:
#             student_list.append(student)
#     return student_list


def find_students_by_name(student, required_name, index=0):
    if index >= len(student):
        return []
    student_found = find_students_by_name(student, required_name, index + 1)
    current_student = student[index]
    if current_student.name == required_name:
        student_found.append(current_student)
    return student_found


student_named_harry = find_students_by_name(students, 'Harrier Dubois')

print(student_named_harry)
