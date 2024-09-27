class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #O(n * 2^n ) b/c 2^n possibilites, each taking O(n) to calculate
        res = []
        def backtrack(start, curr_subset):
            res.append(curr_subset.copy()) #to avoid all empty lists in results
            
            for i in range(start, len(nums)):
                # append
                curr_subset.append(nums[i])
                # go further in recursive stack
                backtrack(i + 1, curr_subset)
                # explored this tree, pop and explore diff branch now
                curr_subset.pop()
        
        backtrack(0, [])
        return res