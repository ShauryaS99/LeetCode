import heapq as hq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #O(nlogn)
        def calculate_ratio_gain(passed_students, tot_students):
            curr_ratio = passed_students / tot_students
            new_ratio = (passed_students + 1) / (tot_students + 1)
            gain = new_ratio - curr_ratio
            return -gain
            
        # intialize classes as min heap (-gain, {passes, totalStudents})
        ratio_heap = []
        for x, y in classes:
            gain = calculate_ratio_gain(x, y)
            hq.heappush(ratio_heap, (gain, x, y))
        
        # pop heap elements, push new heap elements
        while extraStudents > 0:
            _, x, y = hq.heappop(ratio_heap)
            x += 1
            y += 1
            gain = calculate_ratio_gain(x, y)
            hq.heappush(ratio_heap, (gain, x, y))
            extraStudents -= 1
        
        # Calculate avg gain
        tot_ratio = 0
        for c in ratio_heap:
            _, x, y = c
            tot_ratio += x / y
        return tot_ratio / len(classes)