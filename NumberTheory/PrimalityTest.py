# find prime number use number theory
import math
from bisect import bisect_left, bisect_right

# l = []
#
# for i in range(1,n+1):
#     if n % i == 0:
#         l.append(i)
#
# print(l)

# def is_prime(n):
#     if n < 2: return False
#     if n <=3: return True
#     if n % 2 == 0: return False
#
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(25))

b = [5,4,3,1,2,5]
t = sorted(set(b))

c = [bisect_right(t,x) for x in b]

print(c)