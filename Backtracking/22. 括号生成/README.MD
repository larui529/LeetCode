# 22. 括号生成

问题描述（简述）：给定 n，生成所有由 n 对括号组成且有效的括号字符串（匹配且顺序合法）。

解题思路（中文）：
- 回溯（构造法）：维护当前构造的字符串，记录已使用的左括号数 left 和右括号数 right；在任意时刻只能添加左括号（如果 left < n），以及只能添加右括号（如果 right < left）。当字符串长度为 2n 时加入结果。
- 这种约束式回溯可以有效避免生成无效序列，保证结果唯一且完整。

复杂度提示：Catalan 数量级，时间复杂度约为 O(4^n / sqrt(n))（卡塔兰数近似）。

English (paraphrased): Given n pairs of parentheses, generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Constraints:
- 1 <= n <= 8

Solution idea: Backtracking with `res`, `path` (string builder), and helper `dfs(left, right)` where `left` and `right` are counts of used '(' and ')' respectively. Keep variable names consistent across files.
