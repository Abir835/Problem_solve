class A:
    def first(self):
        print("Method__A")


# A and B direct
# A and C indirect
class B(A):
    def secound(self):
        print("Secound__B")


# B And C direct
class C(B):
    def third(self):
        print("Method__C")


d = C()
d.first()
d.secound()
d.third()
