class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #O(n^n) idk
        res = []
        
        def backtrack(combo, start_index):
            curr_sum = sum(combo)
            # Found a suitable combo
            if curr_sum == target:
                res.append(list(combo))
            elif curr_sum > target:
                return
            # Finding other combos
            else:
                for i in range(start_index, len(candidates)):
                    combo.append(candidates[i])
                    backtrack(combo, i) #start index prevents combo from looking backwards at numbers
                    combo.pop()
                
        
        backtrack([], 0)
        return res