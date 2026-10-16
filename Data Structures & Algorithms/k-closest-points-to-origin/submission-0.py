import heapq


class Wrapper:

    def __init__(self, p):
        self.p = p
        self.d = p[0]**2 + p[1]**2

    def __lt__(self, other):
        return self.d < other.d


class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for p in points:
            heapq.heappush_max(max_heap, Wrapper(p))
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)
        
        return [w.p for w in max_heap]
