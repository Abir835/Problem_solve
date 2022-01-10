from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show(self):
        pass


class Teacher(Student):
    def show(self):
        return self.name


class Faculty(Student):
    def show(self):
        return self.name + " " + str(self.age)


f = Faculty("Hasan", 23)
print(f.show())
