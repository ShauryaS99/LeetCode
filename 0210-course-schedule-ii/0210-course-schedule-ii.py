class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Intialize adj map
        pre_reqs = {k: [] for k in range(numCourses)}
        for crs, pre in prerequisites:
            pre_reqs[crs].append(pre)
        
        visited = set()
        course_order = []
        
        # Add course to our ordered list when we finish visiting a course
        def add_course(crs):
            if crs not in course_order:
                course_order.append(crs)
        
        # DFS to determine if cycles exist
        def dfs(crs):
            if crs in visited:
                return False
            if pre_reqs[crs] == []:
                add_course(crs)
                return True
            
            visited.add(crs)
            for pre in pre_reqs[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            # Optimization once we know a course can be visited
            pre_reqs[crs] = []
            add_course(crs)
            return True
        
        for i in range(numCourses):
            # If cycle exists
            if not dfs(i):
                return []
        return course_order