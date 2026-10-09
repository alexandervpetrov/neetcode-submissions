
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


def swap(A, i, j):
    # print('swap:', A[i], A[j])
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
        print(f'cmp: i={i}, left={left}')
        if A[i].key < pivot.key:
            if left != i:
                swap(A, left, i)
                print('after swap:', left, A)
            left += 1

    swap(A, left, end)

    return left


def partition_my(A, beg, end, pivot_pos):

    assert beg < end, "AAA"
    assert beg <= pivot_pos <= end, "BBB"

    pivot = A[pivot_pos]
    # print('pivot:', pivot)

    if pivot_pos != end:
        swap(A, pivot_pos, end)

    left_l = beg
    # while left_l < end and A[left_l] < pivot:
    #     left_l += 1

    left_e = left_l
    # while left_e < end and A[left_e] == pivot:
    #     left_e += 1

    for i in range(left_e, end + 1):
        if A[i].key < pivot.key:
            swap(A, left_l, i)
            if left_l != left_e:
                swap(A, left_e, i)
            left_l += 1
            left_e += 1
        elif A[i].key == pivot.key:
            swap(A, left_e, i)
            left_e += 1

    return left_l, left_e


def quick_sort(A, beg, end):

    if beg >= end:
        return A

    # print('QS:', beg, end)

    pivot_pos = end

    # print('before partition:', A)
    left = partition(A, beg, end, pivot_pos)
    # left_l, left_e = partition_my(A, beg, end, pivot_pos)
    # left = left_l
    # print(' after partition:', A[beg:left], [A[left]], A[left+1:end+1])

    quick_sort(A, beg, left - 1)
    quick_sort(A, left + 1, end)

    return A


class Solution:

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return quick_sort(pairs, 0, len(pairs) - 1)

