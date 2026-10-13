
cache = [0] * 50


class Solution:


    
    def climbStairs(self, n: int) -> int:

        if cache[n] > 0:
            return cache[n]

        if n == 1:
            return 1
        if n == 2:
            return 2

        cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return cache[n]
        