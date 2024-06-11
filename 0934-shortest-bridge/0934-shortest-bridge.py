class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #shortest path is abs(diff_x) + abs(diff_y) - 1
        min_flips = float('inf')
        island_one_coordinates = []
        island_two_coordinates = []
        
        def four_dirs(x, y):
            result = []
            if x + 1 < len(grid):
                result.append((x + 1, y))
            if x - 1 >= 0:
                result.append((x - 1, y))
            if y + 1 < len(grid[0]):
                result.append((x, y + 1))
            if y - 1 >= 0:
                result.append((x, y - 1))
            return result
        
        
        visited = set()
        num_islands = 0
        # Get coordinates of island one and island two
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) in visited or grid[x][y] == 0:
                    continue
                queue = [(x, y)]
                coordinates = []
                while queue:
                    cx, cy = queue.pop(0)
                    if (cx, cy) in visited or grid[cx][cy] == 0:
                        continue
                    visited.add((cx, cy))
                    coordinates.append((cx, cy))
                    queue.extend(four_dirs(cx, cy))
                if num_islands == 0:
                    island_one_coordinates = coordinates
                else:
                    island_two_coordinates = coordinates
                num_islands += 1
                    
        # get the min distance out of all possible distances O(n^2)
        for a, b in island_one_coordinates:
            for c, d in island_two_coordinates:
                flips = abs(c - a) + abs(d - b) - 1
                min_flips = min(min_flips, flips)
        return min_flips