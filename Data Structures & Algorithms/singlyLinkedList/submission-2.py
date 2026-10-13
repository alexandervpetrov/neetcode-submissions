
class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.size = 0
    
    def _find_pos(self, index: int):
        pos = 0
        prev = self.head
        cur = prev.next
        while cur is not None and pos < index:
            prev = cur
            cur = cur.next
            pos += 1
        return prev, cur

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        __, cur = self._find_pos(index)
        return cur.val

    def insertHead(self, val: int) -> None:
        prev, cur = self._find_pos(0)
        new_node = Node(val)
        prev.next = new_node
        new_node.next = cur
        self.size += 1

    def insertTail(self, val: int) -> None:
        prev, __ = self._find_pos(self.size)
        prev.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        prev, cur = self._find_pos(index)
        prev.next = cur.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        cur = self.head.next
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        return values
