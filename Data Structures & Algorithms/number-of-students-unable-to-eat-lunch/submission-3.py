
from collections import deque, Counter


class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sc = Counter(students)
        for s in sandwiches:
            if sc[s] > 0:
                sc[s] -= 1
            else:
                break
        return sc[0] + sc[1] 
