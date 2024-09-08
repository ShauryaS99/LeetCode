class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n * mlogm) where m is avg string length
        anagram_dict = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s) 
            sorted_s = ''.join(sorted_s) #sort string 
            anagram_dict[sorted_s].append(s) # all anagrams will be grouped and appended under sorted key
        
        return list(anagram_dict.values())
            