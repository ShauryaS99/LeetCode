class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #O(n)
        res = []
        prev_start = prev_end = -float('inf')
        ptr_1 = ptr_2 = 0
        while ptr_1 < len(firstList) and ptr_2 < len(secondList):
            start1, end1 = firstList[ptr_1]
            start2, end2 = secondList[ptr_2]
            curr_intersection = []
            # Intersection
            if start2 >= start1 and start2 <= end1:
                curr_intersection = [
                    max(start1, start2),
                    min(end1, end2)
                ]
            elif start1 >= start2 and start1 <= end2:
                curr_intersection = [
                    max(start1, start2),
                    min(end1, end2)
                ]
            if curr_intersection:
                res.append(curr_intersection)
            if end1 < end2:
                ptr_1 += 1
            elif end2 < end1:
                ptr_2 += 1
            else:
                ptr_1 += 1
                ptr_2 += 1
        return res
        