class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #O(n) solution
        # Count zeros
        zero_present = False
        for i in arr:
            if i == 0:
                if zero_present:
                    return True
                else:
                    zero_present = True
        # Check if val is in arr
        for idx, val in enumerate(arr):
            if val != 0 and 2 * val in arr:
                return True
        
        return False
        
        
                
        