# 46. 全排列

问题描述（简述）：给定一个不含重复数字的数组 nums，返回其所有可能的全排列（每个排列包含数组中所有元素，顺序不同视为不同排列）。

解题思路（中文）：
- 回溯（Backtracking）：构建当前排列，使用一个布尔数组或集合记录已使用的元素，递归地把未使用的元素加入当前路径，直到路径长度等于 n 则加入结果。
- 也可以通过交换法（swap）就地生成排列，以减少额外空间。

复杂度提示：全排列数量为 n!，时间复杂度至少 O(n * n!)，空间复杂度取决于递归深度和结果存储。

English (paraphrased): Given a list nums of distinct integers, return all possible permutations.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10

Solution idea: Use backtracking with `res`, `path`, and `used` boolean list. Keep the same helper name `dfs()` for uniformity.

```
Time Complexity: $O(n \cdot n!)$Here is the breakdown of why it lands at that complexity:The Number of Leaves ($n!$): For a set of $n$ distinct numbers, there are exactly $n!$ (n-factorial) possible permutations. Since your recursion only stops and adds to the result when it reaches a leaf (when candidates is empty), you will perform the "base case" operations $n!$ times.The Work at Each Node: In your current implementation, you are creating a new list with candidates[:j] + candidates[j+1:] in every iteration of the loop.The Path Copy: When you reach the base case, res.append(selected.copy()) takes $O(n)$ time to clone the lis
```