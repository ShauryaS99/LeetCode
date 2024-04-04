class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #iterate through, if a letter mapping already exists: make sure its consistent
        letter_map  = {}
        
        for i in range(len(s)):
            if s[i] in letter_map:
                if letter_map[s[i]] != t[i]:
                    return False
            elif t[i] in letter_map.values():
                return False
            else:
                letter_map[s[i]] = t[i]
        return True