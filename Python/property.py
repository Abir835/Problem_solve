class Celsius:
    def __init__(self, temp1=0):
        self._temp = temp1

    @property
    def temp1(self):
        print("get temp")
        return self._temp

    @temp1.setter
    def temp1(self, value):
        if value < -273:
            print("error")
        self._temp = value

    # temp1 = property(get_temp, set_temp)
    # temp1 = temp1.getter(get_temp)
    # temp1 = temp1.setter(set_temp)


c = Celsius(5)
print(c.temp1)
c.temp1 = 500
print(c.temp1)
