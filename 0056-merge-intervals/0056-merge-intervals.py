class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        sorted_intervals = deque(sorted(intervals))
        new_intervals = deque([])
        prev = [-1, -1]
        while sorted_intervals:
            nxt = sorted_intervals.popleft()
            start, end = nxt[0], nxt[1]
            if start > prev[1]:
                new_intervals.append(nxt)
                prev = nxt
            else:
                if nxt[1] > prev[1]:
                    new_intervals.pop()
                    new_intervals.append([prev[0], nxt[1]])
                    prev = [prev[0], nxt[1]]            
        return new_intervals
            