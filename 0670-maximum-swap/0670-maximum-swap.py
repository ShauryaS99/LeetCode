class Solution:
    def maximumSwap(self, num: int) -> int:
        #O(n^2) runtime
        num = str(num)
        swap = False
        for i in range(len(num) - 1):
            digit = num[i]
            max_dig = i
            for j in range(i + 1, len(num)):
                if num[j] > num[max_dig]:
                    max_dig = j
                    swap = True
                if num[j] == num[max_dig] and swap:
                    max_dig = j
                    swap = True
            if swap:
                num = list(num)
                num[i], num[max_dig] = num[max_dig], num[i]
                num = ''.join(num)
                return int(num)
        return int(num)