from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque([])
        self.tot = 0
        
        

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.tot += val
            self.queue.append(val)
            return self.tot / len(self.queue)
        else:
            lru = self.queue.popleft()
            self.tot -= lru
            self.tot += val
            self.queue.append(val)
            return self.tot / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)