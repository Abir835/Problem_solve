# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#
# class Child(Parent):
#     def __init__(self, name, age):
#         Parent.__init__(self, name)
#         self.age = age
#
#     def getAge(self):
#         return self.age
#
#
# class Grandchild(Child):
#     def __init__(self, name, age, location):
#         Child.__init__(self, name, age)
#         self.location = location
#
#     def getLocation(self):
#         return self.location
#
#
# gc = Grandchild("Srinivas", 24, "Hyderabad")
# print(gc.getName(), gc.getAge(), gc.getLocation())

# Another Way
# class A:
#     def __init__(self, *args):
#         self.args = args
#
#     def show(self):
#         print(self.args)
#
#
# class B(A):
#     def __init__(self, *args):
#         super(B, self).__init__(args)
#
#
# class C(B):
#     def __init__(self, *args):
#         super(C, self).__init__(args)
#
#
# obj = C('af', 'aiuf', 12)
# obj.show()

# Another Way

class A:
    def __init__(self, name):
        self.name = name

    def Show(self):
        print(self.name)


class B(A):
    def __init__(self, age, name):
        super(B, self).__init__(name)
        self.age = age

    def Show(self):
        print(self.name, self.age)


class C(B):
    def __init__(self, name, age, address):
        super(C, self).__init__(age, name)
        self.address = address

    def Show(self):
        print(self.name, self.age, self.address)


obj = C('Abir Hasan', 22, 'Uttara')
obj.Show()