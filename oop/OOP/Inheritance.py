# Single Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Show_Info_name(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, sid, email, name, age):
        super(Student, self).__init__(name, age)
        self.sid = sid
        self.email = email

    def Show_Info(self):
        print(self.sid, self.email, self.name, self.age)


obj = Student(17, 'abirhasan@gmail.com', 'Abir', 21)
obj.Show_Info()
obj.Show_Info_name()
