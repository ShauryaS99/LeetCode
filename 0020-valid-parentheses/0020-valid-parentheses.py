class Solution:
    def isValid(self, s: str) -> bool:
        open = {}
        open['('] = ')'
        open['{'] = '}'
        open['['] = ']'
        closed = {}
        
        closed[')'] = '('
        closed['}'] = '{'
        closed[']'] = '['
        stack = []

        for char in s:
            if char in open:
                stack.append(open.get(char))
            if char in closed:
                if len(stack) == 0:
                    return False
                next_char = stack.pop()
                if char == next_char:
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
