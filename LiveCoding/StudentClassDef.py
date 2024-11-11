
class Student:
    def __init__(self, name, homework, quizzes, midterm, final):
        self.name = name
        self.homework = homework
        self.quizzes = quizzes
        self.midterm = midterm
        self.final = final

    def __repr__(self):
        return f'Student(name={self.name}, homework={self.homework}, quizzes={self.quizzes}, midterm={self.midterm}, final={self.final})'

    def CreateStudent():
        return [
            Student(name='Alice Smith', homework=[100, 92, 98, 100, 95, 93, 89, 91, 90, 0], quizzes=[
                82, 83, 91, 80, 82, 85, 80, 0], midterm=89, final=93),
            Student(name='Li Wei', homework=[94, 85, 88, 0, 93, 87, 86, 90, 89, 92], quizzes=[
                81, 76, 88, 84, 80, 82, 78, 80], midterm=86, final=88),
            Student(name='Arjun Patel', homework=[78, 0, 89, 92, 95, 92, 88, 89, 91, 93], quizzes=[
                72, 78, 85, 80, 79, 77, 82, 81], midterm=81, final=87),
            Student(name='Chidinma Okafor', homework=[0, 90, 87, 88, 92, 94, 95, 91, 89, 92], quizzes=[
                80, 84, 86, 85, 0, 80, 78, 81], midterm=85, final=84),
            Student(name='Maria Hernandez', homework=[95, 88, 90, 87, 92, 94, 93, 0, 91, 92], quizzes=[
                0, 78, 82, 81, 80, 78, 77, 76], midterm=80, final=86),
            Student(name='Jordan Tremblay', homework=[88, 90, 91, 92, 93, 92, 91, 0, 89, 90], quizzes=[
                76, 80, 81, 80, 78, 0, 76, 75], midterm=82, final=85),
            Student(name='Harrier Dubois', homework=[90, 92, 85, 89, 88, 89, 87, 86, 85, 0], quizzes=[
                72, 78, 80, 0, 76, 78, 79, 77], midterm=79, final=82)
        ]
