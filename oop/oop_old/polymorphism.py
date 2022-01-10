class Animal:
    def leg(self):
        print("have two lwg")


class Man:
    def leg(self):
        print("4 leg")


a = Animal()
b = Man()

for obj in (a, b):
    obj.leg()


# inheritance
class Abir:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)

    def info(self):
        print("Good Humanity")


class Antor(Abir):
    def info(self):
        print("Bad humanity")


a = Abir("Md. Abir Hasan", 23)
a.show()
a.info()
b = Antor("Hasan", 23)
b.show()
b.info()


# Function

class C:
    def leg(self):
        print("C")


class D:
    def leg(self):
        print("D")


def func(abir):
    abir.leg()


e = C()
f = D()
func(e)
func(f)


################################
def add(x=0, y=0, z=0):
    print(x + y + z)


add(10, 20, 10)
add()
add(10, 20)
