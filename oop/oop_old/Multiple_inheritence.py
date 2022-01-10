class Vehicle:
    def __init__(self, name):
        self.vehicle_name = name

    def carName(self):
        print(self.vehicle_name)


class Driver:
    def __init__(self, name):
        self.driver_name = name

    def driverName(self):
        print(self.driver_name)


class Car(Vehicle, Driver):
    def __init__(self, carName, driverName):
        Vehicle.__init__(self, carName)
        Driver.__init__(self, driverName)

    def show(self):
        print("Car Name: "+self.vehicle_name + "\nDriver Name: " + self.driver_name)


a = Car("Tata", "Abir Hasan")
a.carName()
a.driverName()
a.show()
