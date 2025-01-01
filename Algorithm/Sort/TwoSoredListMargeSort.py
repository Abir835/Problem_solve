def sorted_marge_sort(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)
    i,j = 0,0
    while i<len_a and j<len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i<len_a:
        sorted_list.append(a[i])
        i += 1
    while j<len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list

def marge_sort(arr):
    if len(arr) <=1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]
    left = marge_sort(left)
    right = marge_sort(right)
    return sorted_marge_sort(left,right)

    l


print(marge_sort([1,2,3,4,1,2,7,9,8]))

# print(sorted_marge_sort([1,3,4,6], [1,3,4]))