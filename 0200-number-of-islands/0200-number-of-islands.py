class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = []
        num_islands = 0
        
        def four_directions(coordinate):
            result = []
            x,y = coordinate
            north = (x - 1, y)
            south = (x + 1, y)
            east = (x, y + 1)
            west = (x, y - 1)
            if x - 1 >= 0:
                result.append(north)
            if x + 1 < len(grid):
                result.append(south)
            if y + 1 < len(grid[0]):
                result.append(east)
            if y - 1 >= 0:
                result.append(west)
            return result
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                queue.append((i,j))
                #skip points that are in another island or that are water
                if (i,j) not in visited and grid[i][j] == '1':
                    num_islands += 1
    
                #run BFS from every point to see the island
                while queue:
                    coordinate = queue.pop(0)
                    x,y = coordinate
                    if x < 0 or x > len(grid) or y < 0 or y > len(grid[0]):
                        continue
                    if grid[x][y] == '0':
                        continue
                    if coordinate not in visited:
                        visited.add(coordinate)
                        queue.extend(four_directions(coordinate))
        return num_islands