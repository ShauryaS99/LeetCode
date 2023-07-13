import string
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res
        
        map_p = {letter: 0 for letter in string.ascii_lowercase}
        map_s = {letter: 0 for letter in string.ascii_lowercase}
        for letter in p:
            map_p[letter] = map_p.get(letter, 0) + 1
        begin = 0
        end = len(p) - 1
        for num in range(0, end + 1):
            map_s[s[num]] = map_s.get(s[num], 0) + 1
        while end < len(s):
            if map_s == map_p:
                res.append(begin)
            map_s[s[begin]] -= 1
            begin += 1
            end += 1
            if end < len(s):
                map_s[s[end]] += 1
        return res
            
            
        