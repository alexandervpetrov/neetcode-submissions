# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result_head = None
        result_tail = None
        
        while list1 is not None or list2 is not None:
            min_node = None
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    min_node = list1
                    list1 = list1.next
                else:
                    min_node = list2
                    list2 = list2.next
            elif list1 is not None:
                min_node = list1
                list1 = list1.next
            else:
                min_node = list2
                list2 = list2.next

            if result_head is None:
                result_head = min_node
                result_tail = min_node
            else:
                min_node.next = None
                result_tail.next = min_node
                result_tail = min_node

        return result_head


