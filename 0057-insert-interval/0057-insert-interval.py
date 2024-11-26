class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #One pass solution O(n)
        res = []
        
        for start, end in intervals:
            if end < newInterval[0]:  # No overlap, current interval ends before newInterval starts
                res.append([start, end])
            elif start > newInterval[1]:  # No overlap, current interval starts after newInterval ends
                res.append(newInterval)
                newInterval = [start, end]  # Update newInterval to process remaining intervals
            else:  # Overlapping intervals, merge them
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        res.append(newInterval)  # Append the last interval
        return res
