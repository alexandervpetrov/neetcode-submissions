
from collections import deque


class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sw = deque(sandwiches)
        missed = 0
        while st and missed < len(st):
            if st[0] == sw[0]:
                st.popleft()
                sw.popleft()
                missed = 0
            else:
                st.append(st.popleft())
                missed += 1
        return len(st)
