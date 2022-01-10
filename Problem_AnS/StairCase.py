# pattern
#
# #
# ##
# ###
# ####

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("* ", end=" ")
#     print()

####
####
####
####

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("# ", end="")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, " ", end="")
#     print()


# # #
# #
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 2 - i):
#         print("* ", end="")
#     print()

# 1 2 3 4
# 1 2 3
# 1 2
# 1
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 2 - i):
#         print(j, " ", end="")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1
n = int(input())
for i in range(n):
    for j in range(i, -1, -1):
        print(j + 1, " ", end=" ")
    print()

# 4 3 2 1
# 3 2 1
# 2 1
# 1

# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
