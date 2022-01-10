from datetime import date


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def birthdate(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def adult(age):
        return age > 18


a = Student("Abir", 23)
b = Student.birthdate("Hasan", int(input("age...")))
print(a.name, " ", a.age, "adult--->", Student.adult(a.age))
print(b.name, " ", b.age, "adult--->", Student.adult(b.age))

