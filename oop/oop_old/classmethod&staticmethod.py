class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def msg(self):
        print(self.name + " got " + self.marks + "%")

    @classmethod
    def result_per(cls, name, marks):
        return cls(name, str((int(marks) / 600) * 100))

    @staticmethod
    def age_get(age):
        if age > str(17):
            print("young people.")
        else:
            print("Child gye")


s2 = Student.result_per(input("enter name....: "), input("enter marks...: "))
s2.age_get(input("age.....:"))
s2.msg()
