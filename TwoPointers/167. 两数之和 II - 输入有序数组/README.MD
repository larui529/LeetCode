# 167. 两数之和 II - 输入有序数组

问题描述（中文）：给定一个已按非递减顺序排列的整数数组 `numbers`，在数组中找出两个数，使它们的和等于目标数 `target`。返回这两个数的下标（1-indexed），且第一个下标必须小于第二个下标。假定每个输入只对应唯一的答案。

解题思路（中文）：
- 使用双指针：left 指向开头，right 指向结尾。计算 sum = numbers[left] + numbers[right]。
- 若 sum == target，则返回 [left+1, right+1]；若 sum < target，left += 1；否则 right -= 1。
- 时间复杂度：O(n)，空间复杂度：O(1)。
