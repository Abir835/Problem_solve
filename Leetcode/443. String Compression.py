class Solution:
    def compress(self, chars):

        char_length = len(chars)

        count = 1
        index = 0

        for i in range(1, char_length + 1):
            if i < char_length and chars[i] == chars[i - 1]:
                count += 1
            else:

                chars[index] = chars[i - 1]
                index += 1

                if count > 1:
                    for c in str(count):
                        chars[index] = c
                        index += 1

                count = 1

        return index

# Example usage
obj = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
new_length = obj.compress(chars)

print(new_length)  # Output: 4
print(chars[:new_length])  # Output: ['a', 'b', '1', '2']
