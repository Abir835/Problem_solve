class Solution:
    def maxScore(self, s: str) -> int:
        one_count = 0
        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1

        zero_count = 0
        max_count = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_count += 1
            if s[i] == '1':
                one_count -= 1
            current_score = zero_count + one_count
            if current_score > max_count:
                max_count = current_score
        return max_count

obj = Solution()
print(obj.maxScore('00'))