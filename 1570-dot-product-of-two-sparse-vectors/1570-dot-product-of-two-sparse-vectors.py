# Optimized for sparse vectors: dict with only populated numbers
class SparseVector:
    def __init__(self, nums: List[int]):
        self.valid_nums = {idx: nums[idx] for idx in range(len(nums)) if nums[idx] != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        tot_sum = 0
        for idx, val in self.valid_nums.items():
            if idx in vec.valid_nums:
                tot_sum += self.valid_nums[idx] * vec.valid_nums[idx]
        return tot_sum
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)