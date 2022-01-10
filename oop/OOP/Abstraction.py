from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def msg(self):
        pass


class Abir(Base):
    def msg(self):
        print("hello abir")


class Hasan(Base):
    def msg(self):
        print("Hello Hasan")


obj = Abir()
obj.msg()

obj1 = Hasan()
obj1.msg()