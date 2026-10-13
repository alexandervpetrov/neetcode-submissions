# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        old_head, tail = head, head.next
        new_head = self.reverseList(tail)
        tail.next = old_head
        old_head.next = None
        return new_head