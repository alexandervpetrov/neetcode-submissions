class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freqs = [0] * 3

        for n in nums:
            freqs[n] += 1

        pos = 0
        for n, count in enumerate(freqs):
            for __ in range(count):
                nums[pos] = n
                pos += 1
        