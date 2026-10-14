
class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        tail = self.tail
        tail_prev = tail.prev
        new_item = Node(value)
        new_item.prev = tail_prev
        tail_prev.next = new_item
        new_item.next = tail
        tail.prev = new_item
        self.size += 1

    def appendleft(self, value: int) -> None:
        head = self.head
        head_next = head.next
        new_item = Node(value)
        new_item.prev = head
        head.next = new_item
        new_item.next = head_next
        head_next.prev = new_item
        self.size += 1
        
    def pop(self) -> int:
        if self.size == 0:
            return -1
        tail = self.tail
        value = tail.prev.val
        new_prev = tail.prev.prev
        tail.prev = new_prev
        new_prev.next = tail
        self.size -= 1
        return value

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        head = self.head
        value = head.next.val
        new_next = head.next.next
        head.next = new_next
        new_next.prev = head
        self.size -= 1
        return value
