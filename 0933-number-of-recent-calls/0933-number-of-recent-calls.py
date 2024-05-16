class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        oldest_req = self.requests[0]
        while oldest_req < t - 3000:
            self.requests.popleft()
            oldest_req = self.requests[0]
        self.counter = len(self.requests)
        return self.counter
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)