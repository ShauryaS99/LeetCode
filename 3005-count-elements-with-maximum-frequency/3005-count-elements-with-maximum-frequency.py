class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        tot_freq = 0
        max_freq = 1
        freq_map = {}
        for i in nums:
            curr_freq = freq_map.get(i, 0) + 1
            max_freq = max(max_freq, curr_freq)
            freq_map[i] = curr_freq
        for num, freq in freq_map.items():
            if freq == max_freq:
                tot_freq += freq
        return tot_freq