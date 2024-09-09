class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        open_brackets = ['(', '{', '[']
        bracket_dict = {}
        bracket_dict[')'] = '('
        bracket_dict['}'] = '{'
        bracket_dict[']'] = '['
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                # Closed brackets with no open ones
                if len(stack) == 0:
                    return False
                # Closed brackets should match with open ones 
                if bracket_dict[char] != stack.pop():
                    return False
        # Leftover open brackets
        if stack:
            return False
        else:
            return True