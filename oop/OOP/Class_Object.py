class Car:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def result(self):
        return self.height * self.weight


obj = Car(10, 20)
print(obj.result())
