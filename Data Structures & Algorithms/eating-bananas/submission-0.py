import math


class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_time(k: int) -> int:
            return sum(int(math.ceil(x / k)) for x in piles)

        L = 1
        R = max(piles)
        min_speed = R

        while L <= R:
            speed_guess = (L + R) // 2
            t = eating_time(speed_guess)
            if t <= h:
                min_speed = speed_guess
                R = speed_guess - 1
            else:
                L = speed_guess + 1
        
        return min_speed