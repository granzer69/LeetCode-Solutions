class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def dfs(r, c):

            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visited
                or grid[r][c] == "0"
            ):
                return

            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:

                    islands += 1
                    dfs(r, c)

        return islands
