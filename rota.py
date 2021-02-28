# Person Object 
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

# Teacher Object that Inherits Name and Age from Person Object
class Teacher(Person):
    def __init__(self , name , age , wage):
        super().__init__(name , age)
        self.wage = wage

# Student Object that Inherits Name and Age from Person Object
class Student(Person): # If grade given isnt within 0 and 100 dont add it
    def __init__(self , name , age , grade):
        super().__init__(name , age)
        if int(grade) < 0 or int(grade) > 100:
            print("Not a Real Grade")
        else:
            self.grade = grade 

    # Returns Grade
    def get_grade(self):
        return self.grade


# Course Object 
class Course():
    def __init__(self , name , max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    # Adds Student to Course
    def add_student(self , student): # If the Course is not full, Add Student
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    # Get Average Grade
    def get_average_grade(self):
        value = 0
        for student in self.students:       # For every student in the course
            value += student.get_grade()    # Add up there grades and divide 
        return value / len(self.students)   # By the number of students

# Building Students 
s1 = Student("Mark" , 20 , 95)
s2 = Student("Mick" , 21 , 50)
s3 = Student("John" , 39 , 80)
s4 = Student("Mary" , 26 , 65)
s5 = Student("Lisa" , 40 , 70)

# Building Courses
science = Course("Science" , 100)
maths = Course("Maths" , 100)
english = Course("English" , 100)

# Adding Students to Courses
science.add_student(s1)
science.add_student(s2)
science.add_student(s3)
science.add_student(s4)
science.add_student(s5)

# Adding Students to Courses
maths.add_student(s1)
maths.add_student(s4)
maths.add_student(s5)

# Adding Students to Courses
english.add_student(s2)
english.add_student(s3)

# Finding Students and Average Grades
print(f'The Fourth Science Student is {science.students[3].name}')
print('Average Grade for Science is' , science.get_average_grade())

print(f'The First Math Student is {maths.students[0].name}')
print('Average Grade for Math is' , maths.get_average_grade())

print(f'The Second English Student is {english.students[1].name}')
print('Average Grade for English is' , english.get_average_grade())