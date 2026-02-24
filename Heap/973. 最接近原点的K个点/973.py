from typing import List
import heapq


def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    # use heapq.nsmallest for simplicity
    return heapq.nsmallest(K, points, key=lambda p: p[0]*p[0] + p[1]*p[1])


if __name__ == '__main__':
    pts = [[1,3],[-2,2]]
    print(kClosest(pts, 1))  # [[-2,2]]
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(x, y):
            return x**2 + y**2
        heap = []
        for x, y in points:
            dist = get_dist(x, y)
            if len(heap) < k:
                heapq.heappush(heap, [-dist, x, y])
            else:
                if dist < -heap[0][0]:
                    heapq.heapreplace(heap, [-dist, x,y])
        res = []
        for _, x, y in heap:
            res.append([x, y])
        return res