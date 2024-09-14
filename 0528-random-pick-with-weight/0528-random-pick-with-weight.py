import random
class Solution:
#O(n) for init and O(logn) for pickIndex
    def __init__(self, w: List[int]):
        self.sum = sum(w)
        # Each index represents a range of values out of the total sum
        # if the randint falls in the range of values => pick that idx
        self.prefix_sum = []
        curr_sum = 0
        for idx in range(len(w)):
            curr_sum += w[idx]
            self.prefix_sum.append(curr_sum)
        

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.sum)
        # Binary search
        left, right = 0, len(self.prefix_sum)
        while left <= right:
            mid = (left + right) // 2
            if random_num > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()