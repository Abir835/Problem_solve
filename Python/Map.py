"""
def map_result(n):
    return n * 5


result = []
num = [1, 2, 3, 4, 5]
for i in num:
    result.append(map_result(i))
print(result)

"""
"""
def map_function(n):
    return n * 5


num = [1, 2, 3, 4, 5]
result = list(map(map_function, num))
print(result)
"""

num = [1, 2, 3, 4]

lm_fn = lambda x: x*2

print(list(map(lm_fn, num)))
