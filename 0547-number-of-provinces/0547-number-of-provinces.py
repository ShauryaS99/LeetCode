class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num_provinces = 0
        # Recursive call for valid unvisited neighbors 
        def dfs(visited, city):
            visited.add(city)
            connections = isConnected[city]
            for route in range(len(connections)):
                if route in visited or connections[route] == 0:
                    continue
                dfs(visited, route)
        #DFS from each point, skip visited
        for i in range(len(isConnected)):
            if i in visited:
                continue
            else:
                #Every DFS call is an unexplored province
                dfs(visited, i)
                num_provinces += 1
        return num_provinces