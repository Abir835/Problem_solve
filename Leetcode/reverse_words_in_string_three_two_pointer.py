s = "Let's take LeetCode contest"

# data = " ".join([w[::-1] for w in s.split(" ")])
new_s = []
for data in s.split(" "):
    data_ = data[::-1]
    new_s.append(data_)
print(" ".join(new_s))
