class Solution:
    def maximumSwap(self, num: int) -> int:
        #O(n) runtime; O(n) space
        num_lst = list(str(num))
        max_lst = [-1] * len(num_lst)
        
        # Iterate from right, finding max number from the right till that index
        # We do this to swap with the rightmost (lowest value) higest number
        curr_max = -1
        curr_max_idx = -1
        for i in range(len(num_lst) - 1, -1, -1):
            curr = int(num_lst[i])
            if curr > curr_max:
                curr_max = curr
                curr_max_idx = i
            max_lst[i] = (curr_max, curr_max_idx)
        
        # Iterate from left, finding first number that can benefit from swap
        # Find num < max => swap
        for i in range(len(num_lst)):
            # Greater number to right exists => swap
            if max_lst[i][0] > int(num_lst[i]):
                max_index = max_lst[i][1]
                num_lst[i], num_lst[max_index] = num_lst[max_index], num_lst[i]
                break
            
        return int("".join(num_lst))
        