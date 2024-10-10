class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #O(n)
        num_moves = 0
        stack = deque([])
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack:
                    stack.pop()
                else:
                    num_moves += 1
        return len(stack) + num_moves