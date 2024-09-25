# Weird Algorithm
# Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
# $$ 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$
# Your task is to simulate the execution of the algorithm for a given value of n.
# Input
# The only input line contains an integer n.
# Output
# Print a line that contains all values of n during the algorithm.
# Constraints
#
# 1 \le n \le 10^6
#
# Example
# Input:
# 3
#
# Output:
# 3 10 5 16 8 4 2 1


def wired_algorithm(n, list_=None):
    if list_ is None:
        list_ = []

    list_.append(n)

    if n == 1:
        return list_

    if n % 2 == 0:
        return wired_algorithm(n // 2, list_)
    else:
        return wired_algorithm((n * 3) + 1, list_)

n = int(input())
obj = wired_algorithm(n)

for i in obj:
    print(i, end=" ")