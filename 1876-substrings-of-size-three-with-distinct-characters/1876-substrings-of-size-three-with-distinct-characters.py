class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        if len(s) < 3:
            return res
        substring = set()
        for i in range(len(s) - 2):
            if len(set(s[i:i+3])) == 3:
                   res += 1
        return res
            