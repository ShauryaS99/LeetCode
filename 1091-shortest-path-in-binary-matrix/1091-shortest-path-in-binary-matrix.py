from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #O(mn) babyyyyy
        steps = 1
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        # Handle edge cases
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return steps
        
        # Nodes in queue
        while q:
            q_len = len(q)
            # Take a step from each visited point
            for _ in range(q_len):
                x, y = q.popleft()
                for dx, dy in dirs:
                    new_x = x + dx
                    new_y = y + dy
                    if (0 <= new_x < len(grid) and
                    0 <= new_y < len(grid[0]) and
                    (new_x, new_y) not in visited and 
                    grid[new_x][new_y] == 0):
                        q.append((new_x, new_y))
                        # Add visited here so we don't get duplicates when all nodes are adding their neighbors
                        visited.add((new_x, new_y))
            steps += 1
            # We found the bottom right
            if (len(grid) - 1, len(grid[0]) - 1) in visited:
                return steps

        return -1