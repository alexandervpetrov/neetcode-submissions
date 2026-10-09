
class Node:

    def __init__(self, key, val, l=None, r=None):
        self.key = key
        self.val = val
        self.l = l
        self.r = r


def get_min(root):
    if root is None:
        return None
    if root.l is None:
        return root
    return get_min(root.l)


def get_max(root):
    if root is None:
        return None
    if root.r is None:
        return root
    return get_min(root.r)


def find(root, key):
    if root is None:
        return None
    if root.key == key:
        return root
    if root.key > key:
        return find(root.l, key)
    return find(root.r, key)


def insert(root, key, val):
    if root is None:
        return Node(key, val)
    if root.key == key:
        root.val = val
    elif root.key > key:
        root.l = insert(root.l, key, val)
    else:
        root.r = insert(root.r, key, val)
    return root


def remove(root, key):
    if root is None:
        return None
    if root.key > key:
        root.l = remove(root.l, key)
    elif root.key < key:
        root.r = remove(root.r, key)
    else:
        if root.l is None:
            return root.r
        elif root.r is None:
            return root.l
        mn = get_min(root.r)
        root.key = mn.key
        root.val = mn.val
        root.r = remove(root.r, mn.key)
    return root


def inorder(root):
    if root is None:
        return []
    r = []
    r.extend(inorder(root.l))
    r.append(root)
    r.extend(inorder(root.r))
    return r


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = insert(self.root, key, val)

    def get(self, key: int) -> int:
        node = find(self.root, key)
        if node is None:
            return -1
        return node.val

    def getMin(self) -> int:
        if self.root is None:
            return -1
        node = get_min(self.root)
        return node.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        node = get_max(self.root)
        return node.val

    def remove(self, key: int) -> None:
        self.root = remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        return [
            node.key
            for node in inorder(self.root)
        ]
