# lambda function is an anonymous function
# anonymous means a function without name
"""
result = (lambda x, y, z: z * y * z)(2, 3, 4)
print(result)
"""

"""
result = lambda name: "I am " + name
print(result("Abir Hasan"))
"""
"""
num = [1, 2, 3, 4, 5]

lambda_fun = lambda x: (x % 2) != 0

result = list(filter(lambda_fun, num))
print(result)
"""

num = [1, 2, 3, 4, 5]

print(list(filter(lambda x: (x % 2) != 0, num)))
