import inflect

num = inflect.engine()
b = num.number_to_words(int(input("Number....: ")))
print(b)
