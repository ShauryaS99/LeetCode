class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        stack = []
        #put all vowels in stack
        for char in s:
            if char.lower() in vowels:
                stack.append(char)
        new_s = ""
        for i in range(len(s)):
            if s[i].lower() in vowels:
                new_s += stack.pop()
            else:
                new_s += s[i]
        return new_s
            