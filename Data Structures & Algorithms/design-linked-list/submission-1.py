
class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _find_pos(self, index: int):
        pos = 0
        prev = None
        cur = self.head
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

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        if self.size == 0:
            self.head = self.tail = new_head
            self.size += 1
            return
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        if self.size == 0:
            self.head = self.tail = new_tail
            self.size += 1
            return
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        prev, cur = self._find_pos(index)
        new_item = Node(val)
        prev.next = new_item
        new_item.next = cur
        self.size += 1

    def delete_at_head(self) -> None:
        if self.size < 1:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        old_head = self.head
        self.head = old_head
        old_head = None
        self.size -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.delete_at_head()
        prev, cur = self._find_pos(index)
        if index == self.size - 1:
            prev.next = None
            self.tail = prev
        else:
            prev.next = cur.next
            cur.next = None
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)