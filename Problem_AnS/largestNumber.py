def largestNumber(num):
    max_num = num[0]
    sec_max = num[0]
    for data in num:
        if data > max_num:
            max_num = data

    for data in num:
        if sec_max < data < max_num:
            sec_max = data
    return max_num, sec_max


print(largestNumber([1, 4, 5, 6, 6, 8, 9]))
