# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

def merge(A, B, key=lambda x: x):
    res = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if key(A[i]) <= key(B[j]):
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    
    while i < len(A):
        res.append(A[i])
        i += 1

    while j < len(B):
        res.append(B[j])
        j += 1

    return res


def merge_sort(items, key=lambda x: x):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    L = merge_sort(items[:mid], key=key)
    R = merge_sort(items[mid:], key=key)
    return merge(L, R, key=key)


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return merge_sort(pairs, key=lambda p: p.key)
