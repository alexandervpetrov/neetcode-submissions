
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


def swap(A, i, j):
    print('swap:', A[i], A[j])
    A[i], A[j] = A[j], A[i]


def partition(A, beg, end, pivot_pos):

    assert beg < end, "AAA"
    assert beg <= pivot_pos <= end, "BBB"

    pivot = A[pivot_pos]
    print('pivot:', pivot)

    if pivot_pos != end:
        swap(A, pivot_pos, end)

    left = beg
    for i in range(beg, end):
        print('cmp:', i)
        if A[i].key < pivot.key:
            swap(A, left, i)
            left += 1
            print('after swap:', left, A)

    swap(A, left, end)

    return left


def quick_sort(A, beg, end):

    if beg >= end:
        return A

    print('QS:', beg, end)

    pivot_pos = end
    print('before pn:', A)
    left = partition(A, beg, end, pivot_pos)
    print('partition:', A[beg:left], [A[left]], A[left+1:end+1])

    quick_sort(A, beg, left - 1)
    quick_sort(A, left + 1, end)

    return A


class Solution:

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return quick_sort(pairs, 0, len(pairs) - 1)

