class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = 0
        s_iter = 0
        while i < len(t) and s_iter < len(s):
            if t[i] == s[s_iter]:
                s_iter += 1
            i += 1
        if s_iter == len(s):
            return True
        else:
            return False