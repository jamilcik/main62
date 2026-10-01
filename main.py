
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Shaxs: {self.name}, Yoshi: {self.age}"
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)
class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
        self.teaching_courses = []

    def assign_course(self, course):
        self.teaching_courses.append(course)
class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits
        self.students = []
        self.professor = None

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def set_professor(self, professor):
        self.professor = professor
        professor.assign_course(self)
student1 = Student("Ali", 20, "ST12345")
prof1 = Professor("Dr. Valiyev", 45, "Matematika kafedrasi")
math_course = Course("Oliy matematika", 6)
math_course.set_professor(prof1)
student1.enroll(math_course)
print(prof1.get_info())
print(f"O'qitayotgan fani: {prof1.teaching_courses[0].course_name}")
print(f"Fanga yozilgan talaba: {math_course.students[0].name}")