class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Uses additional space
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for k, v in dic.items():
            if v == 1:
                return k
        return 0
