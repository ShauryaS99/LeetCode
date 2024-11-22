class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        for interval in intervals:
            start, end = interval
            if start > prev_end:
                res.append([prev_start, prev_end])
                prev_start = start
                prev_end = end
            elif start <= prev_end:
                prev_end = max(prev_end, end)
        res.append([prev_start, prev_end])
        return res