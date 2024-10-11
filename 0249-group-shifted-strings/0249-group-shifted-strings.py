import string
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        #O(n * k) where k is len(longest_str) time, O(n) space
        diff_to_str = defaultdict(list)
        # Iterate through strings, store (tuple of idx diff) => [lists of strings]
        for s in strings:
            if len(s) == 1:
                diff_to_str[(-1)].append(s)
                continue
            diff_tuple = []
            # Store tuple of idx diff
            for i in range(1, len(s)):
                diff_tuple.append((ord(s[i]) - ord(s[i - 1])) % 26)
            diff_to_str[tuple(diff_tuple)].append(s)
        
        return diff_to_str.values()
            
                
                    