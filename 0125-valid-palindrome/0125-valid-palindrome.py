class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Remove non-alphanumeric characters
        s = s.lower()
        clean_s = ""
        for i in s:
            if i.isalnum():
                clean_s += i
        # 2 pointer approach
        left = 0
        right = len(clean_s) - 1
        while left <= right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True