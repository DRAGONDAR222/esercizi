from student import Student
from professor import Professor
from course import Course
from department import Department
from university import University


if __name__ == '__main__':

    # Courses objects
    python_course = Course(course_name='Python', course_code='#0001')
    ai_course = Course(course_name='Artificial Intelligence', course_code='#0002')
    data_science_course = Course(course_name='Data Science', course_code='#0003')

    # Student objects
    king: Student = Student(name='King', age=20, student_id='KNG1')
    queen: Student = Student(name='Queen', age=22, student_id='QEN2')
    jack: Student = Student(name='Jack', age=19, student_id='JCK3')

    # Professor objects
    zoro: Professor = Professor(name='Zoro', age=30, professor_id='ZRO1')
    nami: Professor = Professor(name='Nami', age=35, professor_id='NMI2')
    sanji: Professor = Professor(name='Sanji', age=40, professor_id='SNJ3')

    # Department objects
    coding: Department = Department(department_name='Coding')

    # University object
    university: University = University()


    # Assigning Professor objects to Course objects
    python_course.set_professor(professor=zoro)
    ai_course.set_professor(nami)
    sanji.assign_to_course(course=data_science_course)

    # Assigning Student objects to Course objects
    python_course.add_student(student=king)
    python_course.add_student(student=queen)
    jack.enroll(course=python_course)
    king.enroll(course=ai_course)
    ai_course.add_student(jack)
    data_science_course.add_student(queen)

    # Assigning Course objects to Department objects
    coding.add_course(course=python_course)
    coding.add_course(course=ai_course)
    coding.add_course(course=data_science_course)

    # Assigning Professor objects to Department objects
    coding.add_professor(professor=zoro)
    coding.add_professor(professor=nami)
    sanji.setDepartment(department=coding)
    
    # Assigning department objects to University objects
    university.add_department(department=coding)

    # Assigning Student objects to University objects
    university.add_student(student=king)
    university.add_student(student=queen)
    university.add_student(student=jack)

    # Printing University object
    print(university)
    
