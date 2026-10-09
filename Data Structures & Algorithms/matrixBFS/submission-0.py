
import collections


class Solution:

    def shortestPath(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])

        beg = (0, 0)
        end = (R-1, C-1)

        dirs = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )

        q = collections.deque()
        q.append(beg)
        pathlen = 0
        visited = set()

        while q:
            for __ in range(len(q)):
                p = q.popleft()
                if p == end:
                    return pathlen
                r, c = p
                for dp in dirs:
                    dr, dc = dp
                    rr, cc = r + dr, c + dc
                    if rr < 0 or cc < 0:
                        continue
                    if rr >= R or cc >= C:
                        continue
                    if grid[rr][cc] == 1:
                        continue
                    nextp = (rr, cc)
                    if nextp in visited:
                        continue
                    q.append(nextp)
                    visited.add(nextp)
            pathlen += 1

        return -1