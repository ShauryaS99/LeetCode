class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Create a dict from nums1 list for O(1) lookup
        nums1_dict = {k:1 for k in nums1}
        for i in nums2:
            if i in nums1_dict:
                return i
        return -1