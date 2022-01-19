"""
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
filter(function, iterable)
def abir(n):
    if n % 2 != 0:
        return n


num = [1, 2, 3]
num1 = []

for i in num:
    num1.append(abir(i))
print(num1)


"""

num = [1, 2, 3, 4]

g = lambda x: (x % 2) != 0

print(list(filter(g, num)))
