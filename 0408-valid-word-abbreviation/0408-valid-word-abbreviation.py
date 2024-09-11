class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #O(n), 2 ptr approach
        word_idx = 0
        abbr_idx = 0
        while word_idx < len(word) and abbr_idx < len(abbr):
            # Handle case if numeric
            if abbr[abbr_idx].isdigit():
                # Leading 0
                if abbr[abbr_idx] == "0":
                    return False
                curr_num = ""
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    curr_num += abbr[abbr_idx]
                    abbr_idx += 1
                curr_num = int(curr_num)
                word_idx += curr_num
            elif word[word_idx] != abbr[abbr_idx]:
                return False
            else:
                word_idx += 1
                abbr_idx += 1
        # Length of abbreviation didn't match word
        if word_idx != len(word) or abbr_idx != len(abbr):
            return False
        return True