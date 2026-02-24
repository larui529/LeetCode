from typing import List
from collections import Counter
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    # use most_common if allowed
    return [x for x, _ in cnt.most_common(k)]


if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
