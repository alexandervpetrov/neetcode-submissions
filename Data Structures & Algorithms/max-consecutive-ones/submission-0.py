class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                max_ones = max(max_ones, count)
                count = 0
        max_ones = max(max_ones, count)
        return max_ones        

        