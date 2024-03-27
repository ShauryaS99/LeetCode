class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        #O(k) because once we find k factors we return
        factor_set = []
        for i in range(1, n + 1):
            if n % i == 0:
                factor_set.append(i)
            if len(factor_set) == k:
                return factor_set[k - 1]
        return -1
            
            