from typing import List

class UF:
    def __init__(self, n: int):
        self.parent = list(range(n+1))
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        return True

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UF(n)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []

if __name__ == '__main__':
    print(findRedundantConnection([[1,2],[1,3],[2,3]]))  # [2,3]
