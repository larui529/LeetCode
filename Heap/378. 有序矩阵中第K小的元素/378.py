from typing import List
import heapq


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    heap = []  # (val, r, c)
    for r in range(min(n, k)):  # at most k rows needed
        heapq.heappush(heap, (matrix[r][0], r, 0))
    val = 0
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))
    return val


if __name__ == '__main__':
    mat = [[1,5,9],[10,11,13],[12,13,15]]
    print(kthSmallest(mat, 8))  # 13

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        val = 0
        heap = []
        y_ins = [0] * n

        for i in range(min(m, k)):
            heapq.heappush(heap, [matrix[i][0], i, 0])
        # print(heap)
        for j in range(k):
            # print(heapq.heappop(heap))
            val, x, y = heapq.heappop(heap)
            if y < n-1:
                heapq.heappush(heap, [matrix[x][y+1],x, y+1])
            
        return val

