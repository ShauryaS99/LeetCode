class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #O(nk) where k is the longest letter in the list
        longest_prefix = strs[0]
        for i in range(1, len(strs)):
            curr_prefix = ""
            for a, b in zip(longest_prefix, strs[i]):
                if a == b:
                    curr_prefix += a
                else:
                    break
            longest_prefix = curr_prefix
        return longest_prefix
        