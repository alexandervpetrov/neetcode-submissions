
import collections


class Graph:
    
    def __init__(self):
        self.g = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.g:
            self.g[src] = set()
        if dst not in self.g:
            self.g[dst] = set()
        self.g[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.g:
            self.g[src] = set()
        if dst not in self.g:
            self.g[dst] = set()
        was_present = (dst in self.g[src])
        self.g[src].discard(dst)
        return was_present

    def hasPath(self, src: int, dst: int) -> bool:
        hp1 = self.has_path_bfs(src, dst)
        return hp1

    def has_path_bfs(self, src: int, dst: int) -> bool:
        visited = set()
        visited.add(src)
        queue = collections.deque()
        queue.append(src)
        while queue:
            for __ in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True
                for adj in self.g[node]:
                    if adj in visited:
                        continue
                    visited.add(adj)
                    queue.append(adj)
        return False
