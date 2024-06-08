class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize adjacency list
        prereq_dict = {k: [] for k in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_dict[crs].append(pre)
        
        visited = set()
        rec_stack = set()
        
        # Cycle detection: if node in visited set already
        def dfs(crs):
            if crs in rec_stack:
                return False
            if crs in visited:
                return True
            
            rec_stack.add(crs)
            for pre in prereq_dict[crs]:
                if not dfs(pre):
                    return False
            rec_stack.remove(crs)
            visited.add(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        