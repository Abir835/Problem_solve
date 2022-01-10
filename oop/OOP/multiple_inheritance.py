# Single Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Show_Info(self):
        print(self.name, self.age)


class Student:
    def __init__(self, sid, email):
        self.sid = sid
        self.email = email

    def Show_Info(self):

        print(self.sid, self.email)


class Base(Person, Student):
    def __init__(self, name, age, sid, email, fullname):
        Person.__init__(self, name, age)
        Student.__init__(self, sid, email)
        self.fName = fullname

    def Show_Info(self):
        print(self.sid, self.age, self.name, self.fName, self.email)


obj = Base('abir', 21, 17103272, 'abir@gmail.com', 'Abir Hasan')
obj.Show_Info()
