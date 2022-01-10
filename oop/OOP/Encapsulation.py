class Mango:
    def __init__(self):
        self.__price = 1000

    def show(self):
        print(self.__price)

    def set_value(self, value):
        self.__price = value


obj = Mango()
obj.show()
obj._Mango__price = 2000
obj.show()
# obj.set_value(2000)
# obj.show()
