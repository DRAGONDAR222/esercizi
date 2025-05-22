'''Exercise 4: University Management System
Create a system to manage a university with departments, courses, professors, and students.  

1. Create an abstract class Person:
Attributes:

name
age
Methods:

get_role, an abstract method to be implemented by subclasses.
__str__, method to return a string representation of the person.
2. Create subclasses Student and Professor that inherit from Person and implement the abstract method.

Class Student:
Additional attributes:

student_id,
courses (list of Course instances).
Additional method:

enroll, to enroll the student in a course.
Class Professor:
Additional attributes:

professor_id,
department (a Department instance), 
courses (list of Course instances)
Additional method:

assign_to_course, to assign the professor to a course.

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
4. Create a class Department:

Attributes:

department_name
courses (list of Course instances)
professors (list of Professor instances)
Methods:

add_course, to add a course to the department.
add_professor, to add a professor to the department.
__str__, method to return a string representation of the department.
5. Create a class University:

Attributes:

name
departments (list of Department instances)
students (list of Student instances)
Methods:

add_department, to add a department to the university.
add_student, to add a student to the university.
__str__, method to return a string representation of the university.
Finally, write a simple driver program. After creating a University, you should begin by creating instances of the main components that make up a university:

Departments (e.g., Computer Science, Literature)

Courses (e.g., Data Structures, Medieval Literature)

Professors (e.g., faculty members who will teach the courses)

Students (e.g., individuals who will enroll in the courses)

Once these instances are created, follow these steps:

Add all entities to the university: Ensure the university class can register departments and students. 

Enroll students in courses: Simulate student registration by assigning students to one or more courses. 

Assign professors to courses: Each course should have a professor responsible for teaching it. 

Display the state of the university: at each significant step, print out a summary of the university’s current state. This might include:

A list of courses with assigned professors.
Which students are enrolled in which courses.
A breakdown of departments and the courses they offer.'''



from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name:str = name
        self.age:int = age 

    @abstractmethod
    def get_role(self):
        pass
    
    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}"
    

class Student(Person):
    def __init__(self,name:str,age:int,s_id:int):
        self.s_id:int = s_id
        self.courses:list[Course] = []
        super().__init__(name,age)

    def enroll(self, course_enroll: "Course") -> None:              # Forward reference "Classe_seguente"
        if self not in course_enroll.students:
            course_enroll.students.append(self)
            self.courses.append(course_enroll)

    def get_role(self) -> type:                                     # "type" si riferisce a qualsiasi oggetto classe
        return self.__class__

class Professor(Person):
    def __init__(self,name:str,age:int,p_id:int):
        self.p_id:int = p_id
        self.courses:list[Course] = []
        self.department: Department
        super().__init__(name,age)

    def assign_to_course(self,course_assign:"Course") -> None:
            course_assign.professor = self
            self.courses.append(course_assign)
    
    def get_role(self) -> type:                                    
        return self.__class__

class Course:
    def __init__(self, course_name:str,course_code:int):
        self.course_name:str = course_name
        self.course_code: int = course_code
        self.students:list[Student] = []
        self.professor:Professor = None

    def add_student(self,student_to_add:Student) -> None:
        if student_to_add not in self.students:
            self.students.append(student_to_add)
    
    def set_professor(self,professor_to_set:Professor) -> None:
        self.professor = professor_to_set

    def __str__(self) -> str:
        return f"Name: {self.course_name}, Code: {self.course_code}, Students: {self.students}, Professor: {self.professor}"

class Department:
    def __init__(self,department_name:str):
        self.department_name:str = department_name
        self.courses:list[Course] = []
        self.professors:list[Professor] = []

    def add_course(self,course_to_add:Course) -> None:
        self.courses.append(course_to_add)

    def add_professor(self,professor_to_add:Professor) -> None:
        self.professors.append(professor_to_add)

    def __str__(self) -> str:
        return f"Name: {self.department_name}, Courses: {self.courses}, Professors: {self.professors}"
    

class University:
    def __init__(self,name:str):
        self.name:str = name
        self.departments:list[Department] = []
        self.students:list[Student] = []

    def add_department(self,department_to_add:Department) -> None:
        self.departments.append(department_to_add)

    def add_student(self,student_to_add:Student) -> None:
        self.students.append(student_to_add)

    def __str__(self) -> str:
        return f"Name: {self.name}, Departments: {self.departments}, Students: {self.students}"
    

# Creazione di un'istanza dell'università
università = University("Università Tecnologica")

# Creazione dei dipartimenti
informatica = Department("Informatica")
letteratura = Department("Letteratura")

# Aggiunta dei dipartimenti all'università
università.add_department(informatica)
università.add_department(letteratura)

# Creazione dei corsi
strutture_dati = Course("Strutture Dati", 101)
letteratura_medievale = Course("Letteratura Medievale", 201)

# Aggiunta dei corsi ai rispettivi dipartimenti
informatica.add_course(strutture_dati)
letteratura.add_course(letteratura_medievale)

# Creazione dei professori
prof_smith = Professor("Dr. Smith", 45, 1001)
prof_jones = Professor("Dr. Jones", 50, 1002)

# Assegnazione dei professori ai corsi
prof_smith.assign_to_course(strutture_dati)
prof_jones.assign_to_course(letteratura_medievale)

# Aggiunta dei professori ai dipartimenti
informatica.add_professor(prof_smith)
letteratura.add_professor(prof_jones)

# Creazione degli studenti
studente_alice = Student("Alice", 20, 2001)
studente_bob = Student("Bob", 22, 2002)

# Aggiunta degli studenti all'università
università.add_student(studente_alice)
università.add_student(studente_bob)

# Iscrizione degli studenti ai corsi
studente_alice.enroll(strutture_dati)
studente_bob.enroll(letteratura_medievale)

# Visualizzazione dello stato dell'università
print("\nDettagli dell'Università:")
print(università)

print("\nDipartimenti:")
for dipartimento in università.departments:
    print(dipartimento)

print("\nCorsi e Professori Assegnati:")
for dipartimento in università.departments:
    for corso in dipartimento.courses:
        print(f"{corso.course_name} - Professore: {corso.professor.name}")

print("\nStudenti Iscritti ai Corsi:")
for dipartimento in università.departments:
    for corso in dipartimento.courses:
        studenti_nomi = [studente.name for studente in corso.students]
        print(f"{corso.course_name}: {', '.join(studenti_nomi) if studenti_nomi else 'Nessuno studente iscritto'}")

