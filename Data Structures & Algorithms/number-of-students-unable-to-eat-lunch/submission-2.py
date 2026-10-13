
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
        missed = 0
        while st and missed < len(st):
            if st[0] == sw[0]:
                st.popleft()
                sw.popleft()
                missed = 0
            else:
                st.rotate(-1)
                # st.append(st.popleft())
                missed += 1
        return len(st)
