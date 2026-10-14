class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pos = m + n - 1
        i = m - 1
        j = n - 1

        res = nums1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                res[pos] = nums2[j]
                j -= 1
            else:
                res[pos] = nums1[i]
                i -= 1
            pos -= 1
        
        while j >= 0:
            res[pos] = nums2[j]
            j -= 1
            pos -= 1
