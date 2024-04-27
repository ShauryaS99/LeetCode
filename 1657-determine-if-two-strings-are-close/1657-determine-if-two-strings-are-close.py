class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        #Create frequency dictionary
        def get_frequencies(word, freq_dict):
            for letter in word:
                freq_dict[letter] = freq_dict.get(letter, 0) + 1
            return freq_dict
        freq_dict_1 = get_frequencies(word1, {})
        freq_dict_2 = get_frequencies(word2, {})
        print(freq_dict_1)
        print(freq_dict_2)
        
        #Check same letters
        for letter in freq_dict_2.keys():
            if letter not in freq_dict_1:
                return False
        #Check same frequencies
        freq_1 = sorted(list(freq_dict_1.values()))
        freq_2 = sorted(list(freq_dict_2.values()))
        return freq_1 == freq_2
                
        
        
        