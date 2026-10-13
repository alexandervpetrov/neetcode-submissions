# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        if len(pairs) == 0:
            return []
        
        sorted_size = 1
        steps = [list(pairs)]

        while sorted_size < len(pairs):
            item_to_insert = pairs[sorted_size]
            i = sorted_size - 1
            while i >= 0 and pairs[i].key > item_to_insert.key:
                pairs[i + 1] = pairs[i]
                i -= 1
            pairs[i + 1] = item_to_insert
            sorted_size += 1
            steps.append(list(pairs))

        return steps