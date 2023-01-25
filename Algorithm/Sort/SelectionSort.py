A = [1, 2, 3, 4, 5, 1, 9]

for i in range(len(A)):
    min_index = i
    for j in range(i + 1, len(A)):
        if A[min_index] > A[j]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i]

print("sort")
value = []
for i in range(len(A)):
    # print(A[i], end=" ")
    value.append(A[i])
print(value)
