from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        day = 0
        # initialize visited set
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy
                    
                    if 0 <= new_x < len(grid) and \
                    0 <= new_y < len(grid[0]) and \
                    grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.append((new_x, new_y))
            if len(q) > 0:
                day += 1
        
        # check if there are still any fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return day
        
        