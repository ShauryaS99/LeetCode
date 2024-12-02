from collections import defaultdict
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #O(n) solution
        # Create freq dict (b/c of zero edge case, frequency matters)
        freq_dict = defaultdict(int)
        for i in arr:
            freq_dict[i] += 1
        
        for i in arr:
            if i == 0:
                if freq_dict[0] >= 2:
                    return True
            elif 2 * i in freq_dict:
                return True
        
        return False
        
        
                
        