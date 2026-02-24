from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j]:
                uf.union(i, j)
    roots = set()
    for i in range(n):
        roots.add(uf.find(i))
    return len(roots)

if __name__ == '__main__':
    grid = [[1,1,0],[1,1,0],[0,0,1]]
    print(findCircleNum(grid))  # 2
