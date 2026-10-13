
class Node:

    def __init__(self, url: str) -> None:
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        current = self.cur
        new_tail = Node(url)
        new_tail.prev = current
        current.next = new_tail
        self.cur = new_tail

    def back(self, steps: int) -> str:
        moved = 0
        while self.cur.prev is not None and moved < steps:
            self.cur = self.cur.prev
            moved += 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        moved = 0
        while self.cur.next is not None and moved < steps:
            self.cur = self.cur.next
            moved += 1
        return self.cur.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)