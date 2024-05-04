class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_palindrome = s[0]
        #Use each letter as the middle of the palindrome
        for i in range(len(s)):
            #Check single letter middle
            left, right = i - 1, i + 1
            curr_len = 1
            while left <= right:
                #Check out of bounds
                if left < 0 or right >= len(s):
                    break
                if s[left] != s[right]:
                    break
                curr_len += 2
                left -= 1
                right += 1
            if curr_len > max_len:
                max_len = curr_len
                max_palindrome = s[i - max_len//2: i + max_len//2 + 1]
            #Check 2 letter middle
            j = i + 1
            if j < len(s) and s[i] == s[j]:
                left, right = i - 1, j + 1
                curr_len = 2
                while left <= right:
                    #Check out of bounds
                    if left < 0 or right >= len(s):
                        break
                    if s[left] != s[right]:
                        break
                    curr_len += 2
                    left -= 1
                    right += 1
                if curr_len > max_len:
                    max_len = curr_len
                    max_palindrome = s[i - (max_len - 1)//2: j + (max_len - 1)//2 + 1]
            
            
        return max_palindrome