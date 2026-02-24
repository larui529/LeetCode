from typing import List
from collections import defaultdict

class UF:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    uf = UF(n)
    for a, b in pairs:
        uf.union(a, b)
    groups = defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(i)
    res = list(s)
    for comp in groups.values():
        chars = sorted(res[i] for i in comp)
        for idx, ch in zip(sorted(comp), chars):
            res[idx] = ch
    return ''.join(res)

if __name__ == '__main__':
    print(smallestStringWithSwaps("dcab", [[0,3],[1,2]]))  # "bacd"
