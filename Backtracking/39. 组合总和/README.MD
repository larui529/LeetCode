# 39. 组合总和

问题描述（简述）：给定一组无重复的候选数字 candidates 和一个目标数 target，找出 candidates 中所有和为 target 的组合。每个数字可以被重复选取任意次。

解题思路（中文）：
- 回溯（Backtracking）：对 candidates 按顺序遍历，递归选择当前数字 k（可以重复使用）或跳过，注意避免产生重复组合（通过固定顺序、不回溯到之前的候选索引实现）。
- 剪枝：若当前和已超过 target，则可以停止当前分支；对 candidates 排序有助于提前剪枝。

复杂度提示：组合数量依赖输入，回溯树深度和分支因子与 target 和最小候选数有关。

English (paraphrased): Given a list of distinct candidate numbers and a target, return all unique combinations where candidates numbers sum to target. The same number may be chosen unlimited times.

Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[7],[2,2,3]]

Constraints:
- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- 1 <= target <= 500

Solution idea: Sort candidates and use backtracking with `res`, `path`, `start` index for choices; allow reuse by passing `i` as next `start`.
