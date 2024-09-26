
inp = input()

vowels = ["a", "i", "e", "o", "u"]
inp_list = list(inp)

left, right = 0, len(inp_list) - 1

while left < right:
    if inp_list[left].lower() not in vowels:
        left += 1

    elif inp_list[right].lower() not in vowels:
        right -= 1
    else:
        inp_list[left], inp_list[right] = inp_list[right], inp_list[left]
        left += 1
        right -= 1

print( ''.join(inp_list))

# find_vowels = []
# for i in range(len(inp)):
#     if inp[i].lower() in vowels:
#         find_vowels.append(inp[i])
#
# inp_list = list(inp)
# len_vowels = len(find_vowels)
#
# for i in range(len(inp_list)):
#     if inp_list[i].lower() in vowels:
#         inp_list[i] = find_vowels[len_vowels - 1]
#         len_vowels = len_vowels - 1
#
# reversed_vowels_str = ''.join(inp_list)
# print(reversed_vowels_str)
