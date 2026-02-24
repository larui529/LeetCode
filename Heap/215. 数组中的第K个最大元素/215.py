from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    # min-heap of size k
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        else:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
    return heap[0]


if __name__ == '__main__':
    print(findKthLargest([3,2,1,5,6,4], 2))  # 5


import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        n = len(nums)
        for i in range(n):
            if len(max_heap) < k:
                heapq.heappush(max_heap, nums[i])
                continue
            if nums[i] > max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, nums[i])
        return max_heap[0]
            
            