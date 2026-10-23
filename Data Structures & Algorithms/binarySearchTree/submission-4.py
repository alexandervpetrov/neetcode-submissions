
class TreeNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


def insert(root, key, val):
    if root is None:
        return TreeNode(key, val)
    if root.key == key:
        root.val = val
    elif root.key > key:
        root.left = insert(root.left, key, val)
    else: 
        root.right = insert(root.right, key, val)
    return root


def find(root, key):
    if root is None:
        return None
    if root.key == key:
        return root
    elif root.key > key:
        return find(root.left, key)
    else:
        return find(root.right, key)


def find_min_node(root):
    current = root
    while current is not None and current.left is not None:
        current = current.left
    return current


def find_max_node(root):
    current = root
    while current is not None and current.right is not None:
        current = current.right
    return current


def delete(root, key):
    if root is None:
        return None
    if root.key > key:
        root.left = delete(root.left, key)
    elif root.key < key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_node = find_min_node(root.right)
            root.key = min_node.key
            root.val = min_node.val
            root.right = delete(root.right, min_node.key)
    return root


def dfs_inorder(root, callback):
    if root is None:
        return
    dfs_inorder(root.left, callback)
    callback(root)
    dfs_inorder(root.right, callback)


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
        node = find_min_node(self.root)
        if node is None:
            return -1
        return node.val

    def getMax(self) -> int:
        node = find_max_node(self.root)
        if node is None:
            return -1
        return node.val

    def remove(self, key: int) -> None:
        self.root = delete(self.root, key)

    def getInorderKeys(self) -> List[int]:
        keys = []
        dfs_inorder(self.root, lambda node: keys.append(node.key))
        return keys
