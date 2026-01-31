# 78. 子集

问题描述（简述）：给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。解集不能包含重复的子集，子集的顺序可以任意。

解题思路（中文）：
- 回溯（Backtracking）：从索引 0 开始，递归枚举每个元素的“选/不选”两种状态，维护当前路径并把每次递归到的路径加入结果。适用于需要枚举所有组合的题目。
- 迭代法：也可以从空集开始，对数组中每个元素，将其加入到当前所有已有子集中，生成新的子集。

复杂度提示：结果大小为 O(2^n)，时间和空间复杂度都至少与输出大小成比例。

English (paraphrased): Given an integer array nums with no duplicates, return all possible subsets (the power set).

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Solution idea (中文 + English brief): Use backtracking to build a path and at each index choose to include or skip the element. Use consistent variable names: `res` for results, `path` for current selection, helper `dfs(start)`.
