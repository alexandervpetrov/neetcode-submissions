class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for o in operations:
            if o == "C":
                s.pop()
            elif o == "D":
                s.append(2 * s[-1])
            elif o == "+":
                s.append(s[-1] + s[-2])
            else:
                n = int(o)
                s.append(n)
        return sum(s)
