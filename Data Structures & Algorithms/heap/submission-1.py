

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def left_child_idx(i):
    return (i + 1) * 2 - 1

def right_child_idx(i):
    return left_child_idx(i) + 1

def parent_idx(i):
    return (i + 1) // 2 - 1

def percolate_up(data, i):
    while i > 0:
        pi = parent_idx(i)
        if data[pi] <= data[i]:
            break
        swap(data, pi, i)
        i = pi

def min_child_idx(data, i):
    li = left_child_idx(i)
    ri = right_child_idx(i)
    li_valid = li < len(data)
    ri_valid = ri < len(data)
    mci = None
    if li_valid and ri_valid:
        l = data[li]
        r = data[ri]
        mci = li if l <= r else ri
    elif li_valid:
        mci = li
    return mci

def percolate_down(data, i):
    while i < len(data):
        mci = min_child_idx(data, i)
        if mci is None:
            break
        if data[i] <= data[mci]:
            break
        swap(data, i, mci)
        i = mci

def heapify(data):
    beg = parent_idx(len(data)-1)
    for i in range(beg, -1, -1):
        percolate_down(data, i)


class MinHeap:
    
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        percolate_up(self.data, len(self.data)-1)

    def pop(self) -> int:
        if not self.data:
            return -1
        swap(self.data, 0, len(self.data)-1)
        x = self.data.pop()
        percolate_down(self.data, 0)
        return x

    def top(self) -> int:
        if not self.data:
            return -1
        return self.data[0]
        
    def heapify(self, nums: List[int]) -> None:
        self.data = nums
        heapify(self.data)
        