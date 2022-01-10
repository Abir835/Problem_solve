class Student:
    school = "Rajbari Govt. School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def school_name(cls):
        return cls.school

    @staticmethod
    def set_value():
        print("Rajbari District Final Result")


s1 = Student(10, 20, 30)
s2 = Student(10, 10, 10)
Student.set_value()
print(s1.avg(), Student.school_name())
Student.set_value()
print(s2.avg(), Student.school_name())
