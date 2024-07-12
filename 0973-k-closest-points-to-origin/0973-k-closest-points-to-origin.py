import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #O(n)
        dist_list = []
        for i in range(len(points)):
            x, y = points[i]
            distance = x**2 + y**2
            dist_list.append((distance, (x, y)))
        heapq.heapify(dist_list)
        res = []
        for i in range(k):
            dist, point = heapq.heappop(dist_list)
            res.append(point)
        return res