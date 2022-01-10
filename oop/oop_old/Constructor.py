class Employee:
    def __init__(self, name, Id):
        self.id = Id
        self.name = name

    def display(self):
        print("Name: %s ID: %d" % (self.name, self.id))


emp1 = Employee("Abir Hasan", 23)
emp1.display()

emp2 = Employee("Abir Hasan", 25)
emp2.display()


class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1


s1 = Student()
s2 = Student()
s3 = Student()
print("The number of students:", Student.count)


# Python Non-Parameterized Constructor
class Student:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
        print("Hello", name)


student = Student()
student.show("John")


# Python Parameterized Constructor

class Student:
    # Constructor - parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name

    def show(self):
        print("Hello", self.name)


student = Student("John")
student.show()
