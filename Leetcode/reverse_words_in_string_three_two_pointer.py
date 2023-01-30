s = "Let's take LeetCode contest"

# data = " ".join([w[::-1] for w in s.split(" ")])
new_s = []
for data in s.split(" "):
    data_ = data[::-1]
    new_s.append(data_)
print(" ".join(new_s))

# def reverse_word(word):
#     new_word_ = []
#     for data in word.split(" "):
#         left = 0
#         right = len(data) - 1
#
#         word = list(data)
#
#         while left < right:
#             word[left], word[right] = word[right], word[left]
#             left += 1
#             right -= 1
#         new_word = "".join(word)
#         new_word_.append(new_word)
#
#     return " ".join(new_word_)
#
#
# word = input("Enter a word: ")
# print("Reversed word:", reverse_word(word))
