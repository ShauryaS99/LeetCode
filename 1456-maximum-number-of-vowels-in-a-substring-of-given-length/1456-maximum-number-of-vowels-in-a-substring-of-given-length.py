class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def check_vowel(char):
            if char in 'aeiou':
                return True
            return False
        #Sliding Window
        curr_vowels = max_vowels = sum([check_vowel(c) for c in s[:k]])
        for c in range(k, len(s)):
            if check_vowel(s[c]):
                curr_vowels += 1
            if check_vowel(s[c - k]):
                curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        
        return max_vowels