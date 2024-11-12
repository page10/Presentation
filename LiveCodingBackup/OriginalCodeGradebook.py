from StudentClassDef import Student
students = Student.CreateStudent()


def find_student(students: list, require_name: str) -> list:
    student_list = []
    for student in students:  # there is no state
        if student.name == require_name:
            student_list.append(student)
    return student_list


def find_students_by_name(index, require_name, students) -> list:
    if index >= len(students):  # base case
        return []

    next_index = index + 1
    student_found = find_students_by_name(next_index, require_name, students)

    current_student = students[index]
    if current_student.name == require_name:
        student_found.append(current_student)
    return student_found


def find_student_by_final(index, students) -> list:
    if index >= len(students):  # base case
        return None

    next_index = index + 1
    student_found = find_student_by_final(next_index, students)

    current_student = students[index]
    if current_student.final > 83:
        return student_found.append(current_student)
    return student_found


def find_students_with_final_greater_than_midterm(index, students) -> list:
    if index >= len(students):  # base case
        return None

    next_index = index + 1
    student_found = find_students_with_final_greater_than_midterm(
        next_index, students)

    current_student = students[index]
    if current_student.final > current_student.midterm:
        return student_found.append(current_student)
    return student_found


def find_student_by_average_homework(index, students) -> list:
    if index >= len(students):  # base case
        return None

    next_index = index + 1
    student_found = find_student_by_average_homework(
        next_index, students)

    current_student = students[index]
    if sum(current_student.homework) / len(current_student.homework) > 80:
        return student_found.append(current_student)
    return student_found
