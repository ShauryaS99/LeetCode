class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        #calculating the sum takes O(n) and we do that for up to n methods so n^2
        res = [-1] * len(nums)
        if 2*k + 1 > len(nums):
            return res
        window_sum = sum(nums[:2*k + 1])
     # first sum available
#     max_sum = window_sum
 
#     # Compute the sums of remaining windows by
#     # removing first element of previous
#     # window and adding last element of
#     # the current window.
#     for i in range(n - k):
#         window_sum = window_sum - arr[i] + arr[i + k]
#         max_sum = max(window_sum, max_sum)
        for i in range(k, len(nums) - k):
            print(i)
            avg = window_sum / (2*k + 1)
            res[i] = int(avg)
            window_sum -= nums[i - k]
            if i + k + 1 < len(nums):
                window_sum += nums[i + k + 1]
           
        return res