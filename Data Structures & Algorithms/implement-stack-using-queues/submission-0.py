from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()
        self.tmp = deque()

    def push(self, x: int) -> None:
        self.tmp.append(x)
        while self.q:
            self.tmp.append(self.q.popleft())
        self.q, self.tmp = self.tmp, self.q

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()