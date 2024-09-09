class Solution:
    def simplifyPath(self, path: str) -> str:
        #O(n) runtime
        dirs = deque([])
        i = 0
        while i < len(path):
            # Skip slashes
            while i < len(path) and path[i] == "/":
                i += 1
            # Extract directory or ".." or "."
            dir_name = ""
            while i < len(path) and path[i] != "/":
                dir_name += path[i]
                i += 1
            # Handle ".."
            if dir_name == "..":
                if dirs:
                    dirs.pop()
            # Ignore "." or empty strings (double slashes)
            elif dir_name and dir_name != ".":
                dirs.append(dir_name)
        
        # Stitch together all directories
        res = "/" + "/".join(dirs)
        return res