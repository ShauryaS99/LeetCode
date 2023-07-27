class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        stack = []
        visited = set()
        max_area = 0
        
        def explore_directions(x,y):
            directions = []
            north = (x -1, y)
            south = (x + 1, y)
            east = (x, y + 1)
            west = (x, y - 1)
            if x - 1 >= 0:
                directions.append(north)
            if x + 1 < len(grid):
                directions.append(south)
            if y + 1 < len(grid[0]):
                directions.append(east)
            if y - 1 >= 0:
                directions.append(west)
            return directions
                
        #Run DFS on every point: skipping 0s and nodes we have already visited
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                stack.append((i,j))
                #keep a curr_area counter for each island we come across
                curr_area = 0
                while stack:
                    x,y = stack.pop()
                    if grid[x][y] == 0 or (x,y) in visited:
                        continue
                    if (x,y) not in visited:
                        visited.add((x,y))
                        stack.extend(explore_directions(x,y))
                    curr_area += 1 #don't count area if node has been visisted or if 0
                max_area = max(max_area, curr_area)
                    
        return max_area
    