
class Bucket:

    def __init__(self):
        self.items = []

    def put(self, key, value):
        n = len(self.items)
        for i in range(n):
            k, __ = self.items[i]
            if key == k:
                self.items[i] = (key, value)
                return False
        self.items.append((key, value))
        return True

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v
        return None
    
    def remove(self, key):
        n = len(self.items)
        for i in range(n):
            k, __ = self.items[i]
            if key == k:
                del self.items[i]
                return True
        return False


class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._init_data()

    def _init_data(self):
        self.size = 0
        self.data = [Bucket() for __ in range(self.capacity)]

    def _hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bkt = self.data[idx]
        added = bkt.put(key, value)
        if added:
            self.size += 1
        if self.size * 2 >= self.capacity:
            self.resize()

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bkt = self.data[idx]
        v = bkt.get(key)
        if v is None:
            return -1
        return v

    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        bkt = self.data[idx]
        removed = bkt.remove(key)
        if removed:
            self.size -= 1
        return removed

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_data = self.data
        self.capacity *= 2
        self._init_data()
        for bkt in old_data:
            for k, v in bkt.items:
                self.insert(k, v)
