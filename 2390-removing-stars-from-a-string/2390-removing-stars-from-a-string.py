class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == "*" and stack:
                stack.pop()
            elif char != "*":
                stack.append(char)
        return ''.join(stack)
            