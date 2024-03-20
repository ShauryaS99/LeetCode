class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize list w/ 0 because keeping track of cumulative sums
        sum_lst = []
        curr_sum = 0
        sum_lst.append(curr_sum)
        for i in nums:
            curr_sum += i
            sum_lst.append(curr_sum)
        freq_map = {}
        num_subarrays = 0
        # If subarray sum has increased by k then we found a valid subarray
        for i in sum_lst:
            if (i - k) in freq_map.keys():
                num_subarrays += freq_map[i-k]
            if i in freq_map.keys():
                freq_map[i] = freq_map[i] + 1
            else:
                freq_map[i] = 1
        return num_subarrays