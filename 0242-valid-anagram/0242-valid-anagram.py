class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        map_s = {}
        for letter in s:
            map_s[letter] = map_s.get(letter, 0) + 1
        map_t = {}
        for letter in t:
            map_t[letter] = map_t.get(letter, 0) + 1
        if map_s == map_t:
            return True
        else:
            return False
            
        