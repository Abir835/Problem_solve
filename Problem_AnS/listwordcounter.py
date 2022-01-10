name = input()
dic = {}
for letter in name:
    if letter not in dic:
        dic[letter] = 1
    else:
        dic[letter] += 1
print(dic)
