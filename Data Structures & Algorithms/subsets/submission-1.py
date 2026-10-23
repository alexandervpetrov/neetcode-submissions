class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        x = nums[0]
        subsets_without_x = self.subsets(nums[1:])

        subsets_with_x = [
            ss + [x]
            for ss in subsets_without_x
        ]

        return subsets_without_x + subsets_with_x