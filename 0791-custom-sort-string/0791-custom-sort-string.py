class Solution:
    def customSortString(self, order: str, s: str) -> str:
        alphabet_dict = {} # 'a' : (order, freq)
        last_index = 0
        for i in range(len(order)):
            alphabet_dict[order[i]] = (i, 0)
            last_index += 1
        
        for i in range(len(s)):
            if s[i] in alphabet_dict:
                order, freq =  alphabet_dict.get(s[i])
                alphabet_dict[s[i]] = (order, freq + 1)
            else:
                order, freq = last_index, 1
                alphabet_dict[s[i]] = (order, freq)
                last_index += 1                
                        
        res = ''
        sorted_dict = dict(sorted(alphabet_dict.items(), key=lambda x:x[1][0]))

        for i in sorted_dict.items():
            curr_letter = i[0]
            order, freq = i[1]
            substr = curr_letter * freq
            res += substr
        return res