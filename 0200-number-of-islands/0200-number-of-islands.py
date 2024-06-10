class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def adj_lands(x, y):
            dirs = []
            if x + 1 < len(grid) and grid[x + 1][y] == "1":
                dirs.append((x + 1, y))
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                dirs.append((x - 1, y))
            if y + 1 < len(grid[0]) and grid[x][y + 1] == "1":
                dirs.append((x, y + 1))
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                dirs.append((x, y - 1))
            return dirs
        
        visited = set()
        counter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                queue = [(i, j)]
                while queue:
                    cx, cy = queue.pop(0)
                    if (cx, cy) in visited:
                        continue
                    visited.add((cx, cy))
                    valid_dirs = adj_lands(cx, cy)
                    queue.extend(valid_dirs)
                counter += 1
        return counter
