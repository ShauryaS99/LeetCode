class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #O(n)
        abbr_word = ""
        curr_number = ""
        # Construct word from abbr
        for char in abbr:
            if curr_number and int(curr_number) > len(word):
                return False
            if char.isalpha():
                # Add wild chars to abbr word
                if curr_number:
                    new_s = "*" * int(curr_number)
                    abbr_word += new_s
                    curr_number = ""
                abbr_word += char
            elif char.isdigit():
                # Leading zero
                if not curr_number and char == "0":
                    return False
                curr_number += char

        if curr_number:
            if int(curr_number) > len(word):
                return False
            new_s = "*" * int(curr_number)
            abbr_word += new_s
        
        print(abbr_word)
        print(len(abbr_word))
        print(len(word))
        if len(abbr_word) != len(word):
            return False
        
        # Check char for char if words match
        for i in range(len(abbr_word)):
            if abbr_word[i] == "*":
                continue
            elif abbr_word[i] != word[i]:
                return False
        
        return True