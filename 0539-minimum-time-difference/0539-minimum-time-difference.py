class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #O(nlogn) b/c of sorting
        min_difference = 720
        def epoch_calc(time):
            hours = int(time[:2])
            minutes = int(time[3:])
            return (hours * 60) + minutes
        
        timePoints = [epoch_calc(i) for i in timePoints]
        timePoints.sort()
        time_a = timePoints[0]
        for i in range(1, len(timePoints)):
            time_b = timePoints[i]
            diff = (time_b - time_a)            
            min_difference = min(min_difference, diff)
            time_a = time_b
            
        # Find diff btwn last and first element
        time_a = timePoints[0]
        time_b = timePoints[-1]
        diff = 1440 - (time_b - time_a)            
        min_difference = min(min_difference, diff)
        time_a = time_b
        
        return min_difference
                    