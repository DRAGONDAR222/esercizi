'''
3. Create a class Course:
Attributes:

course_name
course_code
students (list of Student instances)
professor (Professor instance)
Methods:

add_student, to add a student to the course.
set_professor, to set the professor for the course.
__str__, method to return a string representation of the course.
'''

if __name__ == '__main__':
    from student import Student
    from professor import Professor

class Course:

    def __init__(self, course_name: str, course_code: str):
        self._course_name = course_name
        self._course_code = course_code
        self._professor: Professor = ''
        self._students: list[Student] = []

    def add_student(self, student: 'Student') -> None:
        if student not in self._students:
            self._students.append(student)
            if self not in student._courses:
                student.enroll(self)

    def set_professor(self, professor: 'Professor') -> None:
        self._professor = professor

    def __str__(self) -> str:
        student_str = '\n'.join(str(student) for student in self._students)
        return f'Course name: {self._course_name} - Course Code: {self._course_code} - Course instructor: {self._professor}\n--> Student list\n{student_str}\n'
    

if __name__ == '__main__':
    c1: Course = Course('Course1', '#1')
    s1: Student = Student('King', 20, '@1')
    s1.enroll(c1)
    print(c1)