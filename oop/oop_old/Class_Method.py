# s = 'ABIR HASAN'
#
# a = s.__len__()  # this is called properties
# print(a)
#
# b = len(s)  # this is called method
# print(b)


class Vehicle:
    # def set_value(self, name, wheel, color):
    #     self.Name = name
    #     self.Wheel = wheel
    #     self.Color = color

    def show(self):
        print(self.Name, self.Wheel, self.Color)

    # def name(self):
    #     print(self.Name)


car = Vehicle()
# car.set_value('Honda', 2, 'Yellow')
car.Name = "Abir"
car.Wheel = 4
car.Color = "blue"
car.show()

var = Vehicle()
var.Name = "hasan"
var.Wheel = 4
var.Color = "blue"
var.show()


# car.name()


class Name:
    def __init__(self, name, age, school):
        self.Name = name
        self.Age = age
        self.School = school

    def result(self):
        return self.Name + " \n" + str(self.Age) + " \n" + self.School


obj = Name("Md. Abir Hasan", 24, "IUBAT")
print(obj.result())
