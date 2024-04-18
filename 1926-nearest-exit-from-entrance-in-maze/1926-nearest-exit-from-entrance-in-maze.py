class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        q = [entrance]
        visited = set([(entrance[0], entrance[1])])
        num_steps = 0
        while q:
            size = len(q) # Store the size of the current level
            num_steps += 1
            for _ in range(size): # Iterate over the current level
                curr = q.pop(0)
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in dirs:
                    x = curr[0] + dx
                    y = curr[1] + dy
                    if x not in range(rows) or y not in range(cols):
                        continue
                    if (x,y) in visited or maze[x][y] == "+":
                        continue
                    if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                        return num_steps
                    q.append([x,y])
                    visited.add((x, y))
        
        return -1