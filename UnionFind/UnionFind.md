# 并查集（Union-Find）模板速查（中文）

目的：把并查集问题的常见变体与统一代码模板浓缩为一页，方便面试复习与快速套用。

核心概念：
- `find(x)`：找到节点 `x` 的根（代表元），通常实现路径压缩以加速后续查询。
- `union(a,b)`：把 `a` 和 `b` 所在的集合合并，常配合按秩（rank）或按大小（size）合并以保证树高较小。
- 常用操作：判断连通（find(a)==find(b)）、合并并返回是否发生合并、统计不同根的数量或把节点按根分组。

标准模板（推荐）：

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

    # 可选：统计不同根
    def count_roots(self) -> int:
        return len({self.find(i) for i in range(len(self.parent))})
```

常见模式与注意点：
- 直接节点索引：当输入节点是 0..n-1（如题目给固定编号）可直接使用上面模板。
- 坐标或字符串映射：若节点是坐标或邮箱等非连续 ID，先用 `dict` 映射到连续整数 id，再并查（见 `1202`、`721`）。
- 返回值设计：`union` 返回 `True/False` 很方便（例：`684 冗余边` 按序处理边，遇到 `union` 返回 `False` 即为答案）。
- 计数/分组：合并完成后常要通过 `find` 把节点聚合到根对应的桶（dict 或 defaultdict）以构造输出（例：`1202`、`721`）。

常见题型与小贴士：
- 连接分量计数（例：`547 朋友圈`）：把所有直接相连的对 `union`，最后统计根个数。
- 检测环/冗余边（例：`684 冗余连接`）：顺序遍历边，若 `find(u)==find(v)` 则当前边造成环。
- 行/列连接（例：`947 移除最多的石子`）：用行/列字典把相同行或列的石子映射到第一个出现的索引并 `union`。
- 倒序分配/排序分组（例：`1202 交换字符串最小索引`）：按连通分量收集索引，排序索引与该组字符然后分配最小字符到最小索引。
- 邮箱聚类（例：`721 账户合并`）：email->首次账户 id 的映射 + 并查，最后按根聚合所有邮箱并排序输出。

性能与边界：
- 路径压缩 + 按秩/按大小合并可以把复杂度摊销到几乎常数（α(n)）。
- 当节点数量很大且 ID 稀疏（如坐标范围巨大）时，务必先用哈希表压缩 ID，避免创建巨大的 parent 数组。

面试答题要点（简短陈述练习）：
1. 说明为什么用并查集（需要多次连通/合并查询）。
2. 说明 `find` 的路径压缩与 `union` 的按秩合并以保证性能。
3. 说明题目如何映射到「节点/边」模型（必要时展示映射代码）。
4. 最后说明如何收集结果（统计根或按根分组）。

仓库内参考实现（示例文件）：
- `UnionFind/547. 朋友圈/547.py`  — 连接分量计数示例
- `UnionFind/684. 冗余连接/684.py` — 检测环（遇到未合并的边即返回）
- `UnionFind/947. 移除最多的石子/947.py` — 行列映射示例
- `UnionFind/1202. 交换字符串的最小索引/1202.py` — 按连通分量排序字符并重新分配
- `UnionFind/721. 账户合并/721.py` — 邮箱->账号映射 + 分组示例

把这个 `UnionFind.md` 当作面试的速查卡：记住「映射、合并、聚合（map->union->group）」三步套路即可。
