def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)

    for i in range(m - n + 1):
        if haystack[i:i + n] == needle:
            return i

    return -1


print(strStr('sadbutsad', 'sad'))

# haystack = "leetcode", needle = "leeto"
