class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #O(n) b/c O(1) lookup for each of n elements to check
        # if any num has same [prefix_sum % k]
        prefix_dict = {0: -1}
        curr = 0
        # Create dict => {prefix_sum % k, idx}
        for i in range(len(nums)):
            curr += nums[i]
            # prefix_dict[j] % k == prefix_dict[i] % k
            if curr % k in prefix_dict:
                if i - prefix_dict[curr % k] >= 2:
                    return True
            else:
                prefix_dict[curr % k] = i

        return False