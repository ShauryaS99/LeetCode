class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Bit manipulation XOR
        res = 0
        for n in nums:
            res = res ^ n
        return res
