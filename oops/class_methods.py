# Class methods = Allow operations related to the class itself
#               Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student():
    count = 0
    _Total_gpa = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student._Total_gpa+=gpa

    def get_info(self):
        return f'{self.name}, {self.gpa}'

    @classmethod
    def Total_gpa(cls):
        return cls._Total_gpa

    @classmethod
    def get_avg(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa : {cls._Total_gpa/cls.count:.5f}"

    @classmethod
    def get_count(cls):
        return f"total no. of students : {cls.count}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.Total_gpa())
print(Student.get_avg())


