from __future__ import annotations
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, age:int) -> None:
        self.name:str = name
        self.age:int = age

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Role: {self.get_role()}"
    
class Student(Person):
    def __init__(self, name:str, age:int, student_id:str) -> None:
        super().__init__(name, age)
        self.student_id:str = student_id
        self.courses:list[Course] = []

    def get_role(self) -> str:
        return "Student"
    
    def enroll(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def __str__(self) -> str:
        return super().__str__()+f"ID: {self.student_id}"

class Professor(Person):
    def __init__(self, name:str, age:int, professor_id:str) -> None:
        super().__init__(name, age)
        self.professor_id:str = professor_id
        self.department:Department = None
        self.courses:list[Course] = []

    def get_role(self) -> str:
        return "Professor"
    
    def assign_to_course(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def set_department(self, department:Department) -> None:
        self.department = department

    def __str__(self) -> str:
         if self.department:
            department_name:str = self.department.department_name
            return super().__str__()+f"ID: {self.professor_id}, Department: {department_name}, Courses: {[c.course_name for c in self.courses]}"
         else:
            return super().__str__()+f"ID: {self.professor_id}, Department: 'Dipartimento non ancora assegnato'"

class Course:
    def __init__(self, name:str, code:str) -> None:
        self.course_name:str = name
        self.course_code:str = code
        self.students:list[Student] = []
        self.professor:Professor = None
    
    def add_student(self, student:Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def set_professor(self, professor:Professor) -> None:
        self.professor = professor

    def __str__(self) -> str:
        if self.professor:
            professor_name:str = self.professor.name
            return f"Course name: {self.course_name}, Course ID: {self.course_code}, Professor: {professor_name}, Students: {[s.name for s in self.students]}"
        else:
            return f"Course name: {self.course_name}, Course ID: {self.course_code}, Professor: 'Non ancora assegnato'"

class Department:
    def __init__(self, name:str) -> None:
        self.department_name:str = name
        self.professors:list[Professor] = []
        self.courses:list[Course] = []

    def add_course(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor:Professor) -> None:
        if professor not in self.professors:
            self.professors.append(professor)

    def __str__(self) -> str:
        return f'Department: {self.department_name}, Course: {[c.course_name for c in self.courses]}, Professors: {[p.name for p in self.professors]}'
    
class University:
    def __init__(self, name:str) -> None:
        self.university_name:str = name
        self.departments:list[Department] = []
        self.students:list[Student] = []

    def add_department(self, department:Department) -> None:
        self.departments.append(department)

    def add_student(self, student:Student) -> None:
        self.students.append(student)

    def __str__(self) -> str:
        return f'University: {self.university_name}, Departments: {[d.department_name for d in self.departments]}, Students: {[s.name for s in self.students]}'

if __name__ == '__main__':
    univ:University = University("Sapienza")

    # Crea i dipartimenti
    cs_dep:Department = Department('Informatica')
    lt_dep:Department = Department('Lettere')

    # Aggiungi i dipartimenti all'università
    univ.add_department(cs_dep)
    univ.add_department(lt_dep)

    # Crea i corsi
    python_cs:Course = Course("Programmazione in Python", "PY101")
    antica_cs:Course = Course("Lettere antiche", "LT101")

    # Assegna i corsi ai dipartimenti
    cs_dep.add_course(python_cs)
    lt_dep.add_course(antica_cs)

    # Crea i professori
    mc_prof:Professor = Professor("Marco Cascio", 18, "MC100")
    me_prof:Professor = Professor("Marco Esposito", 30, "ME150")

    # Assegna i professori ai diperimenti
    cs_dep.add_professor(mc_prof)
    lt_dep.add_professor(me_prof)

    # Assegna i dipartimenti ai professori
    mc_prof.set_department(cs_dep)
    me_prof.set_department(lt_dep)

    # Assegna i corsi ai professori
    mc_prof.assign_to_course(python_cs)
    me_prof.assign_to_course(antica_cs)

    # Assegna i professori ai corsi
    python_cs.set_professor(mc_prof)
    antica_cs.set_professor(me_prof)

    # Crea gli studenti
    student_leandro:Student = Student("Leandro Pazienza", 27, "PZN")
    student_cristiano:Student = Student("Cristiano Coccia", 21, "CR7")

    # Aggiunge gli studenti all'università
    univ.add_student(student_leandro)
    univ.add_student(student_cristiano)

    # Assegna gli studenti ai corsi
    student_cristiano.enroll(python_cs)
    student_leandro.enroll(antica_cs)

    # Assegna i corsi agli studenti
    python_cs.add_student(student_cristiano)
    antica_cs.add_student(student_leandro)

    print(univ)
    print(cs_dep)
    print(lt_dep)
    print(python_cs)
    print(antica_cs)
    print(mc_prof)
    print(me_prof)