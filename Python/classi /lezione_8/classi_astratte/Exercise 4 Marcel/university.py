'''
5. Create a class University:

Attributes:

name
departments (list of Department instances)
students (list of Student instances)
Methods:

add_department, to add a department to the university.
add_student, to add a student to the university.
__str__, method to return a string representation of the university.
'''

if __name__ == '__main__':
    from department import Department
    from student import Student

class University: 

    def __init__(self):
        self._departments: list[Department] = []
        self._students: list[Student] = []

    def add_department(self, department: 'Department') -> None:
        if department not in self._departments:
            self._departments.append(department)

    def add_student(self, student: 'Student') -> None:
        if student not in self._students:
            self._students.append(student)

    def __str__(self) -> str:
        departments_str: str = '\n'.join(str(department) for department in self._departments)
        students_str: str = '\n'.join(str(student) for student in self._students)
        return f'--> DEPARTMENTS <--\n{departments_str}--> STUDENTS <--\n{students_str}'