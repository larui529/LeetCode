# 15. 三数之和

问题描述（中文）：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c 使得 a + b + c = 0，找出所有满足条件且不重复的三元组。

解题思路（中文）：
- 先对数组排序。固定一个数 nums[i]，然后对剩下部分使用双指针（left=i+1, right=n-1）寻找两数之和等于 -nums[i] 的组合。
- 跳过重复的固定元素和指针移动过程中的重复值，以保证结果不重复。
- 时间复杂度：O(n^2)，空间复杂度：O(1)（不算返回结果）。

提示：注意处理重复元素和指针移动的边界条件。

For this question, need to do the check of whether ijk sum is 0, then do j+=1 and k-=1 and then remove duplicate. 

So only remove duplicate when you have a ijk sum = 0 (special case, [-2,1,1], if you do dedupe before check sum, then you will miss this case)