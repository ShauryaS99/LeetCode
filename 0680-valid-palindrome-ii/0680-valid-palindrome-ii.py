class Solution:
    def validPalindrome(self, s: str) -> bool:
        #O(n) 2 ptr approach
        def isPalindrome(x):
            l, r = 0, len(x) - 1
            while l <= r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left <= right:
            # if there is a mismatch: advance left or right ptr and check if its now a palindrome
            if s[left] != s[right]:
                return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])
            left += 1
            right -= 1
        return True