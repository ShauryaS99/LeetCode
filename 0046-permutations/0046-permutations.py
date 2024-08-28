class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #O(n!) because we explore all possible permutations
        res = []
        
        def backtrack(curr_permutation):
            # Reached a possible permutation
            if len(curr_permutation) == len(nums):
                res.append(list(curr_permutation))
            # Building a permutation
            else:
                # Iterate through neighbors
                for i in nums:
                    if i in curr_permutation:
                        continue
                    curr_permutation.append(i) #add to solution
                    backtrack(curr_permutation) #recurisve call
                    curr_permutation.pop() #backtrack
                
        backtrack([])
        return res