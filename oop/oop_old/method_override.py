class A:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        return self.name

    def info(self):
        print("Good")


class B(A):
    def info(self):
        print(self.color + " is BAD")


a = B("Abir", "RED")
print(a.show())

a.info()