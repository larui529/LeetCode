# Two Pointers 模板（中文速记）

用途：总结常见的双指针 / 滑动窗口题型的统一思路与代码模板，方便在面试复习时快速回忆。

1) 基本要点（记忆口诀）
- 两指针：`l, r`（或 `left, right`），初始化为区间两端或窗口起点。
- 滑动窗口：用 `left` 和 `right` 扩缩窗口，保持窗口满足某个不变量（无重复、和不超限、包含特定字符等）。
- 每次移动指针后更新答案 `ans` 或 `max_len`。
- 变体主要在于移动哪一侧、是否需要排序、是否需要记录频次/used、以及是否允许重复选取。

2) 统一模板（两端指针，寻找最值 / 区间）

```python
def two_pointer_template(nums):
    l, r = 0, len(nums) - 1
    ans = 0
    while l < r:
        # 计算当前候选值（面积、和、距离等）
        cand = (r - l) * min(nums[l], nums[r])  # 示例：盛水
        ans = max(ans, cand)
        # 决策：移动较小高度的一侧
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return ans
```

3) 统一模板（滑动窗口，满足约束的最长/最多/计数）

```python
def sliding_window_template(s, k):
    # 示例：维护窗口内满足某约束
    left = 0
    freq = {}
    ans = 0
    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        # 当窗口不再满足约束（例如需要替换数 > k）时收缩左边界
        while not window_is_valid(freq, left, right, k):
            freq[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans
```

（注：`window_is_valid` 根据题目不同而实现，例如 `window_len - max_freq <= k`）

4) 常见变体 & 快速记法
- 有序数组两数/三数问题（如 `167` / `15`）：先排序（若输入已排序则跳过），固定一个元素后对剩余用双指针寻找两数之和。
  - 三数和（`15`）记法：for i in range(n): if i>0 and nums[i]==nums[i-1]: continue; target=-nums[i]; l=i+1; r=n-1; while l<r: ... 跳过重复答案。
- 滑动窗口去重（`3` 无重复字符最长子串）：用 `last_index` 字典记录字符上次位置；当遇到重复并且上次位置>=left 时，left=last_index[ch]+1。
- 固定长度/恰好等于 K 的组合：当 `len(window) == K` 时记录并移动左指针。
- 网格/路径 DFS 不是纯双指针，但也使用边界收缩/扩展的思路，通常使用 DFS + 回溯。

5) 常见陷阱
- 只有在输入有序时才可直接使用两端指针寻找和。若无序需先排序（但排序会改变索引，题目若要求索引需注意）。
- 注意重复值去重：在移动指针后要跳过相等的值以避免重复结果（如三数之和）。
- 滑动窗口中频次的 `max_freq` 维护：可以在扩张时更新，在收缩时不必每次重算最大值（只要最终长度更新逻辑正确）；这是常见的优化技巧。
- 指针边界/越界、空数组处理要加验证。

6) 时间/空间复杂度回忆句
- 双指针（两端/查找）通常 O(n) 或 O(n^2)（如固定一项后双指针）
- 滑动窗口通常 O(n)，空间为 O(字符集) 或 O(1)（固定大小计数数组）

7) 面试答题建议
- 列出不变量（窗口保持什么条件）和指针移动的贺决规则（为什么移动这侧）。
- 说明是否需要排序及其影响（时间复杂度/索引影响）。
- 写出统一模板后再按题目替换 `window_is_valid` / 移动规则。

把这份文件作为 TwoPointers 文件夹下的速查表，背诵「指针名字、移动决策、记录/更新答案」三要点即可快速套模做题。
