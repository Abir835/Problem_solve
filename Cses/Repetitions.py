def longest_repeating_sequence(s):
    if len(s) == 0:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    max_len = max(max_len, current_len)
    return max_len


n = input()

print(longest_repeating_sequence(n))