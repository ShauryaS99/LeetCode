class Solution:
    def numSteps(self, s: str) -> int:
        # Time complexity O(N)
        def get_number_from_binary(s):
            return int(s, 2)
        
        def recurse(num, count):
            if num == 1:
                return count
            elif num % 2 == 0:
                return recurse(num // 2, count + 1)
            else:
                return recurse(num + 1, count + 1)
        
        num = get_number_from_binary(s)
        return recurse(num, 0)
