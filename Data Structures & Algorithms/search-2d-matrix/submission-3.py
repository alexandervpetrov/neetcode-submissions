class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        def get(pos):
            i, j = divmod(pos, m)
            return matrix[i][j]

        L = 0
        R = n * m
        while L < R:
            mid = (L + R) // 2
            print(L, R, mid)
            if mid >= R:
                return False
            x = get(mid)
            if x == target:
                return True
            elif x < target:
                L = mid + 1
            else:
                R = mid
        return False
        