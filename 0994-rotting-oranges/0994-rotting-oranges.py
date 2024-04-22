class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        #Add all rotten oranges to deque
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
        
        # Run BFS from multiple sources
        num_mins = 0
        while q:
            size = len(q)
            #For a given level: expand outwards
            for _ in range(size):
                curr = q.popleft()
                dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in dirs:
                    x = curr[0] + dx
                    y = curr[1] + dy
                    if x not in range(rows) or y not in range(cols):
                        continue
                    if grid[x][y] == 0 or (x,y) in visited:
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                    q.append((x,y))
                    visited.add((x,y))
            num_mins += 1
        
        #Check if there are any fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return max(num_mins - 1, 0)