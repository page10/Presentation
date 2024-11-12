### Lambda Function
Presented by Group 7: Yilin Pan, Xiaojing An, Weihang Ding
#### Introduction
Lambda functions provide a concise way to create: 
- Small,  anonymous  functions 
- Without needing to define a formal function using def.

#### Syntax
```python
# this is a def function
def triple(a):
    return a*3

# this is a lambda function
lambda a: a*3
```
**Return:**
Lambda functions *implicitly return the* result of evaluating the expression.
def functions use an explicit return statement.

**Scope:**
Lambda functions are limited to a *single expression*. 
Def functions can contain multiple statements and have more complex logic.

#### Live code example: Gradebook
**Requirement**

In gradebook, find:
1. a student with a given name
2. students who passed final exams
3. students whose final exam scores are higher than mid-term exam scores.
4. students whose have average homework scores greater than 80.

We noticed that each requirement is to find a specific group of students in full students. Instead of writing 4 independent functions with repititive codes, we can write a function which can filter students out, based on another function which defines students selection criteria.

Below is the code snippet of using lambda function to achieve above goals.

```python
def filter(students, predicate, index=0) -> list:
    if index >= len(students):
        return []
    student_found = filter(students, predicate, index + 1)
    current_student = students[index]
    if predicate(current_student):
        student_found.append(current_student)
    return student_found

# Find students by name
student_named_harry = filter(
    students, lambda student: student.name == 'Harrier Dubois')

# Find students with final score greater than 83
students_with_final_greater_than_60 = filter(
    students, lambda student: student.final > 83)

# Find students with final score greater than midterm
students_with_final_greater_than_midterm = filter(
    students, lambda student: student.final > student.midterm)

# Find students with average homework score greater than 80
students_with_average_homework_greater_than_80 = filter(
    students, lambda student: sum(student.homework) / len(student.homework) > 80)
```
*Note: filter is actually a higer-order function in python, which has similar logic as the above filter function. You can search it if you are interested.*