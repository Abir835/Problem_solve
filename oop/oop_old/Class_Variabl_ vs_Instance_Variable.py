class Student:
    uni = "IUBAT"  # Class Variable

    def __init__(self, name, sub, sec):
        self.name = name  # Instance Variable
        self.sub = sub  # Instance Variable
        self.sec = sec  # Instance Variable

    def show(self):
        print("Name: " + self.name + " \nSub: " + self.sub + " \nSec: " + self.sec + " \nUniversity: " + self.uni+"\n\n")


obj = Student(input("Name: "), input("Subject: "), input("Section: "))
obj1 = Student(input("Name: "), input("Subject: "), input("Section: "))
obj2 = Student(input("Name: "), input("Subject: "), input("Section: "))


obj.show()
obj1.show()
obj2.show()
