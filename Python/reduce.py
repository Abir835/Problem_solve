"""
reduce or short code
from functoos import reduce
"""

from functools import reduce

num = [1, 2, 3, 4]
sum1 = reduce(lambda x, y: x + y, num)
print(sum1)
