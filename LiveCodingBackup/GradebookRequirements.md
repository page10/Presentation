# requirements:
find_student(students: list, name: str) -> dict

This functions returns the dictionary of the student with the given name. If the student is not found, it returns None.

# let's see what a student looks like first:
    {
        'name': 'Alice Smith',
        'homework': [100, 92, 98, 100, 95, 93, 89, 91, 90, 0],
        'quizzes': [82, 83, 91, 80, 82, 85, 80, 0],
        'midterm': 89,
        'final': 93
    }

# change into a class for better reading
class Student:
    def __init__(self, name, homework, quizzes, midterm, final):
        self.name = name
        self.homework = homework
        self.quizzes = quizzes
        self.midterm = midterm
        self.final = final

# Example instantiation of the Student class
student = Student(
    name='Alice Smith',
    homework=[100, 92, 98, 100, 95, 93, 89, 91, 90, 0],
    quizzes=[82, 83, 91, 80, 82, 85, 80, 0],
    midterm=89,
    final=93
)

# original code:
def find_student(students: list, require_name: str) -> dict:
    for student in students:
        if student.name == require_name:
            return student
    return None

# this code basically represents: find student by their names
def find_student_by_name:
