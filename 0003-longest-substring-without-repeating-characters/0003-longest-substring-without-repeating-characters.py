class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        substring_set = set()
        ptr_1 = 0
        # Sliding window with 2nd ptr increasing while there are no duplicates
        for ptr_2 in range(len(s)):
            curr_char = s[ptr_2]
            # 1st ptr increases until we get a unique substring again
            while curr_char in substring_set:
                substring_set.remove(s[ptr_1])
                ptr_1 += 1
            substring_set.add(curr_char)
            res = max(res, ptr_2 - ptr_1 + 1)
        return res