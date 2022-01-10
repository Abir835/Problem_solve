class Abir:
    def __init__(self):
        print("abir")


class Hasan(Abir):
    def __init__(self):
        print("Hasan")
        super().__init__()


class Sabbir(Abir):
    def __init__(self):
        print("sabbir")
        super().__init__()


class Antor(Sabbir, Hasan):
    def __init__(self):
        print("Antor")
        super().__init__()


b = Antor()
