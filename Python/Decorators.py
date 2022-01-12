def UpperDecorator(func):
    def wrapper(name, age):
        return name + " " + str(age)
    return wrapper


@UpperDecorator
def text(name):
    return name


print(text("abir", 23))
