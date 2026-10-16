# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []        

        for node in lists:
            if node is not None:
                heapq.heappush(min_heap, NodeWrapper(node))

        dummy_head = ListNode()
        current = dummy_head

        while min_heap:
            nw = heapq.heappop(min_heap)
            node_min = nw.node
            current.next = node_min
            current = node_min
            if node_min.next is not None:
                heapq.heappush(min_heap, NodeWrapper(node_min.next))

        return dummy_head.next


