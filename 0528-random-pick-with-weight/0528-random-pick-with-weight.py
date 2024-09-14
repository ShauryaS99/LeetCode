import random
class Solution:
#O(n) for init and pickIndex
    def __init__(self, w: List[int]):
        self.sum = sum(w)
        # window = index
        self.weight_dict = {}
        curr_max = 0
        for idx in range(len(w)):
            curr_max += w[idx]
            self.weight_dict[curr_max] = idx
        

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.sum)
        for max_num, idx in self.weight_dict.items():
            if random_num <= max_num:
                return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()