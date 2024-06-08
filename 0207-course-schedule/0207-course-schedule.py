class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Initialize adjacency list
        prereq_dict = {k:[] for k in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_dict[crs].append(pre)
        
        visited = set()
        
        #Cycle detection: if node in visited set already
        def dfs(crs):
            if crs in visited:
                return False
            if prereq_dict[crs] == []:
                return True
            
            visited.add(crs)
            for pre in prereq_dict[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prereq_dict[crs] = []
            return True
            
            
        # O(n^2) space complexity: O(n)
        for crs in range(numCourses):
            visited = set()
            if not dfs(crs):
                return False
        return True
        