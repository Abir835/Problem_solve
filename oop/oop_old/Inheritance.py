class Vehicle:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Wheel(Vehicle):
    def value(self):
        print(self.name + " " + "10223")


class Color(Vehicle):

    def colorss(self, color):
        self.color = color

    def colors(self):
        print(self.name + " is " + self.color)


a = Wheel("Tata")
a.show()
a.value()

b = Color("TATA")
b.colorss("RED")
b.colors()
