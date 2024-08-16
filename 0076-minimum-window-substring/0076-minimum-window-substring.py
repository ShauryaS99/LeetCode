class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #O(n)
        if len(t) > len(s):
            return ""
        
        #Initialize Frequency Dict
        t_counts = {}
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1
        
        remaining_chars_dict = t_counts
        valid_chars_ctr = 0
        min_l = 0
        min_window = float('inf')
        #Dynamic Sliding Window
        l = r = 0
        while r < len(s):
            c = s[r]
            # Decrement dict & increment char ctr
            if c in remaining_chars_dict:
                if remaining_chars_dict[c] > 0: #necessary letter
                    valid_chars_ctr += 1
                remaining_chars_dict[c] -= 1
                
            # We have found a valid permutation: try shrinking window
            while valid_chars_ctr == len(t):
                curr_window_size = r - l + 1
                if curr_window_size < min_window:
                    min_window = curr_window_size
                    min_l = l
                leftmost_char = s[l]
                # Increment dict & decrement char ctr
                if leftmost_char in remaining_chars_dict:
                    if remaining_chars_dict[leftmost_char] == 0: #necessary letter
                        valid_chars_ctr -= 1
                    remaining_chars_dict[leftmost_char] += 1
                l += 1 
            r += 1
        
        #Return min window substr
        if min_window < float('inf'):
            return s[min_l: min_l + min_window]
        else:
            return ""
                
        