class Student:

    class_year=2021
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1=Student("Pratham",21)
student2=Student("Shashwat",22)
student3=Student("Anish",23)
student4=Student("Ram",24)
print(student1.class_year)
print(student2.class_year)

print(student1.name)
print(student2.name)

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")