这是一道标准的二分题目。

我们的想法是这样的

1. 不能更改原数组 => 不能排序
2. 只能用O(1)空间 =>不能用hash
3. 时间复杂度小于O(n^2) => 看来是O(nlogn)

那我们能不能在1到n之间猜一个数字k然后比较它和我们要找的重复数dup的大小关系呢？很自然的我们就想到了二分，通过logN的方式逼近我们要找的数字，那猜数字需要logN，判断dup是否小于或等于k就可以用O(N)来完成，也就是遍历整个数组。

假如有一个数组
[1,2,3,3,3,4,5]， dup = 3
假如k等于4，我们发现如果dup<=k，那么如果我们数出所有小于等于k的个数，这个cnt一定大于k。这是因为所有的数都在1到n之间，如果k=4，那么小于或等于4的数假如缺失了，那它一定会出现在dup的位置上，所以小于4的值不管等于几，数目是不变的，利用这个性质我们就可以找到任意数k和重复数dup的大小关系了。

在写二分时我们还是套用模板，如果dupLessOrEqual(mid)这个函数如果返回True，那就说明mid取大了，那我们就right=mid，如果返回False，说明mid取小了，我们就left=mid+1，这里可以加1是因为我们要找的值不在原来[left, mid]这个范围内，我们自然就可以吧mid向更小的区间移动了，因为最后是用left来跳出循环，所以要查mid的取值是否会进入死循环，也就是mid的取值是偏向left还是right。

mid = left+(right-left)//2 左偏
mid = left+(right-left+1)//2 右偏

[LeetCode Link](https://leetcode-cn.com/problems/find-the-duplicate-number/)
