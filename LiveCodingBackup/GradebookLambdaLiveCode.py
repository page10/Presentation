# %% [markdown]

# ### homework requirements:
# ## find_student(students: list, name: str)

# This functions returns the student with the given name. If the student is not found, it returns None.

# story background: Logan ask me to find students based on their gradebook.
# First, I have to find all students with the name 'Alice Smith' in the list of students.
# %% [markdown]
# **let's see what a student looks like first:**

# %%
STUDENTS = [
    {
        'name': 'Alice Smith',
        'homework': [100, 92, 98, 100, 95, 93, 89, 91, 90, 0],
        'quizzes': [82, 83, 91, 80, 82, 85, 80, 0],
        'midterm': 89,
        'final': 93
    },
    {
        'name': 'Li Wei',
        'homework': [94, 85, 88, 0, 93, 87, 86, 90, 89, 92],
        'quizzes': [81, 76, 88, 84, 80, 82, 78, 80],
        'midterm': 86,
        'final': 88
    },
    {
        'name': 'Arjun Patel',
        'homework': [78, 0, 89, 92, 95, 92, 88, 89, 91, 93],
        'quizzes': [72, 78, 85, 80, 79, 77, 82, 81],
        'midterm': 81,
        'final': 87
    },
    {
        'name': 'Chidinma Okafor',
        'homework': [0, 90, 87, 88, 92, 94, 95, 91, 89, 92],
        'quizzes': [80, 84, 86, 85, 0, 80, 78, 81],
        'midterm': 85,
        'final': 84
    },
    {
        'name': 'Maria Hernandez',
        'homework': [95, 88, 90, 87, 92, 94, 93, 0, 91, 92],
        'quizzes': [0, 78, 82, 81, 80, 78, 77, 76],
        'midterm': 80,
        'final': 86
    }]

# %% [markdown]
# **change into a class for better reading**

# %%


class Student:
    def __init__(self, name, homework, quizzes, midterm, final):
        self.name = name
        self.homework = homework
        self.quizzes = quizzes
        self.midterm = midterm
        self.final = final


# %% [markdown]
# **Example instantiation of the Student class**
# %%
students = [
    Student(name='Alice Smith', homework=[100, 92, 98, 100, 95, 93, 89, 91, 90, 0], quizzes=[
            82, 83, 91, 80, 82, 85, 80, 0], midterm=89, final=93),
    Student(name='Li Wei', homework=[94, 85, 88, 0, 93, 87, 86, 90, 89, 92], quizzes=[
            81, 76, 88, 84, 80, 82, 78, 80], midterm=86, final=88),
    Student(name='Arjun Patel', homework=[78, 0, 89, 92, 95, 92, 88, 89, 91, 93], quizzes=[
            72, 78, 85, 80, 79, 77, 82, 81], midterm=81, final=87),
    Student(name='Chidinma Okafor', homework=[0, 90, 87, 88, 92, 94, 95, 91, 89, 92], quizzes=[
            80, 84, 86, 85, 0, 80, 78, 81], midterm=85, final=84),
    Student(name='Maria Hernandez', homework=[95, 88, 90, 87, 92, 94, 93, 0, 91, 92], quizzes=[
            0, 78, 82, 81, 80, 78, 77, 76], midterm=80, final=86)
]


# %% [markdown]
# ## Now! Time to review the original code:
# We want to find all the students with our required name in the list of students.

# %%

# maybe skip this part, use recursion at first

def find_student(students: list, require_name: str) -> list:
    student_list = []
    for student in students:  # there is no state
        if student.name == require_name:
            student_list.append(student)
    return student_list

# %% [markdown]
# **We want to modify this function, using recursion**<br>
# By doing so, we avoid to change the value of "student" in the for loop.<br>
# No side effect, no mutation.

# %%


def filter(index, require_name, students) -> list:
    if index >= len(students):  # base case
        return []

    next_index = index + 1
    student_found = filter(next_index, require_name, students)

    current_student = students[index]
    if current_student.name == require_name:
        student_found.append(current_student)
    return student_found


# %% [markdown]
# Well, **there can be a lot more ways to find students**, apart from the name.<br>
# For example, we want to find students that passed the final exam.<br>
# That is, the final score is greater than 60.<br>
# `student.final > 60`

# %%


def filter_student_by_final(index, students) -> list:
    if index >= len(students):  # base case
        return None

    next_index = index + 1
    student_found = filter_student_by_final(next_index, students)

    current_student = students[index]
    if current_student.final > 60:
        return student_found.append(current_student)
    return student_found

# %% [markdown]
# **Still more ways to filter students!**<br>
# We want to find students that final exam score higher than midterm.<br>
# `student.final > student.midterm`
# **Our code:**

# %%


def filter_student_by_final_higher_than_midterm(index, students) -> list:
    if index >= len(students):  # base case
        return None

    next_index = index + 1
    student_found = filter_student_by_final_higher_than_midterm(
        next_index, students)

    current_student = students[index]
    if current_student.final > current_student.midterm:
        return student_found.append(current_student)
    return student_found


# %% [markdown]
# **STILL MORE!**<br>
# We want to find students that have a higher average homework score than 80.<br>
# `average_score(student.homework) > 80`
# **Our code:**

# %%

def filter_student_by_average_homework(index, students) -> list:
    if index >= len(students):  # base case
        return None

    next_index = index + 1
    student_found = filter_student_by_average_homework(
        next_index, students)

    current_student = students[index]
    if sum(current_student.homework) / len(current_student.homework) > 80:
        return student_found.append(current_student)
    return student_found


# %% [markdown]
# We can notice something now:<br>
# The code is repetitive!<br>
# **The only difference between these functions is the conditions in the if statement.**<br>
# If we pass the condition in a function, **those functions can be merged into one.**<br>


# %% [markdown]
# **Extract the condition part and make it into a seperate function**<br>
# the requirement part: <br>
# `if current_student.name == require_name:`<br><br>
# and, we give our function a better name since it has become more generic:<br>
# `filter_student`

# **Then, our function will be:**

# %%
def student_name_is_equal(student, require_name):
    return student.name == require_name


def filter(students, predicate, index=0) -> list:
    if index >= len(students):
        return []

    student_found = filter(students, predicate, index + 1)

    current_student = students[index]
    if predicate(current_student):  # bug with passing the require_name
        return student_found.append(current_student)

    return student_found


stundent_filtered = filter(STUDENTS, student_name_is_equal)


# %%
# Deal with the parameters
def student_name_is_equal(require_name):
    def check_name(student):
        return student.name == require_name  # Alice Smith
    return check_name


def filter(students, predicate, index=0) -> list:
    if index >= len(students):
        return []

    student_found = filter(students, predicate, index + 1)

    current_student = students[index]
    if predicate(current_student):
        return student_found.append(current_student)

    return student_found


student_filtered = filter(
    STUDENTS, student_name_is_equal('Alice Smith'))


# %%
# Remove the define predicate function part
# using lambda for better reading

def filter(students, predicate, index=0) -> list:
    if index >= len(students):
        return []

    student_found = filter(students, predicate, index + 1)

    current_student = students[index]
    if predicate(current_student):
        return student_found.append(current_student)

    return student_found


student_filtered = filter(
    STUDENTS, lambda student: student.name == 'Alice Smith')

# %% [markdown]
# Same to the other functions:<br>
# `filter_student_by_final`<br>
# `filter_student_by_final_higher_than_midterm`<br>
# `filter_student_by_average_homework`<br>


# %%
def filter(students, predicate, index=0) -> list:
    if index >= len(students):
        return []

    student_found = filter(students, predicate, index + 1)

    current_student = students[index]
    if predicate(current_student):
        student_found.append(current_student)

    return student_found


# Find students by name
students_named_alice = filter(
    students, lambda student: student.name == 'Alice Smith')

# Find students with final score greater than 60
students_with_final_greater_than_60 = filter(
    students, lambda student: student.final > 60)

# Find students with final score greater than midterm
students_with_final_greater_than_midterm = filter(
    students, lambda student: student.final > student.midterm)

# Find students with average homework score greater than 80
students_with_average_homework_greater_than_80 = filter(
    students, lambda student: sum(student.homework) / len(student.homework) > 80)

# %%
