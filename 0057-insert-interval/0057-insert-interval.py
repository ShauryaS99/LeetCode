class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #O(n)
        res = []
        interval_added = False
        # Insert newInterval in correct order
        for start, end in intervals:
            if newInterval[0] < start:
                res.append(newInterval)
                interval_added = True
            res.append([start, end])
        if not interval_added:
            res.append(newInterval)
        
        # Merge intervals
        prev_start, prev_end = res[0][0], res[0][1]
        intervals = []
        for start, end in res:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                intervals.append([prev_start, prev_end])
                prev_start, prev_end = start, end
        intervals.append([prev_start, prev_end])
        return intervals
                
            
        
                
                