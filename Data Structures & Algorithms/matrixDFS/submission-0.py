
class Solution:

    def countPaths(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        visited = set()

        def n_paths_from(r, c):
            if r < 0 or c < 0:
                return 0
            if r >= R or c >= C:
                return 0
            if grid[r][c] == 1:
                return 0
            if (r, c) in visited:
                return 0
            if r == R-1 and c == C-1:
                return 1

            n = 0
            visited.add((r, c))
            n += n_paths_from(r - 1, c)
            n += n_paths_from(r + 1, c)
            n += n_paths_from(r, c - 1)
            n += n_paths_from(r, c + 1)
            visited.remove((r, c))
            return n

        return n_paths_from(0, 0)
