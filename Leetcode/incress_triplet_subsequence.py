class Solution(object):
    def increasingTriplet(self, nums):
        left, mid = float("inf"), float("inf")
        for num in nums:
            if num > mid:
                return True
            elif num < left:
                left = num
            elif left < num < mid:
                mid = num

        return False

obj = Solution()
print(obj.increasingTriplet([3,2,1,5,6,4]))