class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(nlogn) because of sorting at the end
        n = len(nums)
        swap_idx = -1
        #Step 1: find first decreasing val from the right
        right = nums[n - 1]
        for i in range(n - 1, -1, -1):
            left = nums[i]
            # Swap candidate
            if left < right:
                swap_idx = i
                break
            right = left
        
        #Step 2: find smallest value greater than swap candidate
        min_max = float('inf')
        min_max_idx = -1
        for i in range(swap_idx, n):
            # Eligible min_max
            if nums[i] > nums[swap_idx]:
                min_max = min(min_max, nums[i])
                min_max_idx = i
        
        #Step 3: swap the elements
        if swap_idx > -1 and min_max_idx > -1:
            nums[swap_idx], nums[min_max_idx] = nums[min_max_idx], nums[swap_idx]
        
        #Step 4: sort lst to the right of swap
        nums[swap_idx + 1:] = sorted(nums[swap_idx + 1:])
        return nums

