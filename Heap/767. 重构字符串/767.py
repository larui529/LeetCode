from collections import Counter
import heapq


def reorganizeString(s: str) -> str:
    cnt = Counter(s)
    heap = [(-freq, ch) for ch, freq in cnt.items()]
    heapq.heapify(heap)
    res = []
    while len(heap) >= 2:
        f1, c1 = heapq.heappop(heap)
        f2, c2 = heapq.heappop(heap)
        res.append(c1)
        res.append(c2)
        if f1 + 1 < 0:
            heapq.heappush(heap, (f1 + 1, c1))
        if f2 + 1 < 0:
            heapq.heappush(heap, (f2 + 1, c2))
    if heap:
        f, c = heapq.heappop(heap)
        if -f > 1:
            return ""
        res.append(c)
    return ''.join(res)


if __name__ == '__main__':
    print(reorganizeString("aab"))  # aba

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        heap = [(-val, key) for key, val in counts.items()]
        heapq.heapify(heap)

        # print(heap)

        res = []

        while len(heap)>=2:
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)
            res.append(c1)
            res.append(c2)
            if -f1 -1 >0:
                heapq.heappush(heap, (f1+1, c1))
            if -f2-1 > 0:
                heapq.heappush(heap, (f2+1, c2))
        # print(heap)
        if heap:
            f3, c3 = heapq.heappop(heap)
            if -f3 > 1:
                return ""
            res.append(c3)
        return ''.join(res)