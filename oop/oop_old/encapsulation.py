class Student:
    def __init__(self, name):
        self._Student__name = None
        self.name = name
        self._name = name
        self.__name = name

    def name(self):
        return self._name

    def Student__name(self):
        return self._Student__name


a = Student("Abir")
print(a.name)
print(a.name)
print(a.Student__name())
