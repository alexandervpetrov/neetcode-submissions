class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pos = 0
        for n in nums:
            if n != val:
                nums[write_pos] = n
                write_pos += 1
        return write_pos