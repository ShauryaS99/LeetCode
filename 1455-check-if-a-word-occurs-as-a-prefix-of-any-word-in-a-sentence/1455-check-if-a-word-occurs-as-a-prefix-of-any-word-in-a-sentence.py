class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        #O(n)
        sentence_lst = sentence.split(" ")
        search_len = len(searchWord)
        for idx, word in enumerate(sentence_lst):
            if len(word) >= search_len:
                if word[0:search_len] == searchWord:
                    return idx + 1
        return -1