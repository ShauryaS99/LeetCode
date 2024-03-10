class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        # convert to sets because O(1) lookup
        set1 = set(nums1)
        set2 = set(nums2)
        for i in set1:
            if i in set2:
                res.append(i)
        return res