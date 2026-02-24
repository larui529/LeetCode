from typing import List

class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

def removeStones(stones: List[List[int]]) -> int:
    n = len(stones)
    uf = UF(n)
    row = {}
    col = {}
    for i, (r, c) in enumerate(stones):
        if r in row:
            uf.union(i, row[r])
        else:
            row[r] = i
        if c in col:
            uf.union(i, col[c])
        else:
            col[c] = i
    roots = set(uf.find(i) for i in range(n))
    return n - len(roots)

if __name__ == '__main__':
    print(removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))  # 5
