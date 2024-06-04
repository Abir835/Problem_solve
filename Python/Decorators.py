# def UpperDecorator(func):
#     def wrapper(name, age):
#         return name + " " + str(age)
#     return wrapper
#
#
# @UpperDecorator
# def text(name):
#     return name
#
#
# print(text("abir", 23))


# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase

    return wrapper


# decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split

    return wrapper


@splitter_decorator  # this is executed next
@lowercase_decorator  # this is executed first
def hello():
    return 'Hello World'


hello()  # output => [ 'hello' , 'world' ]
