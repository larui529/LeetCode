这是一道典型的可以用扫描线来求解的题目。

扫描线的本质是画一道竖线穿过A，B两个时间区间，如果扫描线扫到了两个区间，表示A，B有交集。通过观察我们可以发现A，B交集的区间开始，结束的点总是A或者B里的区间开始或者结束的时间，所以我们只需要扫A和B两个闭区间列表中所有开始和结束的时间点即可。

所以我们首先把A，B中的开始，结束时间都放入一个nested list中，并且把开始标记为1，结束标记为-1，这样每个时间节点都是一个长度为2的数组（timestamp，S/E_flag)， 并按照时间升序，flag降序进行排列。为什么这样排列下边会讲。

在扫描时，为了计算出我们的线扫过了几个区间，我们会创建一个变量count，当我们在扫开始时间时，我们在count上加1，表示扫描经过的区间又多了一个，当我们在扫结束时间时，我们在count上减1，表示扫描经过的区间少了一个。如果在一个时间点上既有开始，又有结束，那我们要先扫开始加1，再扫结束减1，因为题目中一个时间上的点也是答案之一，所以在排序是我们把flag进行降序排列。

在每次扫描完某个时间节点后我们要判断这个时间节点是不是A，B某个交集的开始或结束。如果count==2，那么这个点就是一个交集开始节点，更新start，如果flag==-1同时count==1，那么这个点就是一个交集结束节点，更新end，同时我们需要把区间的开始，结束时间写入result。

最后返回result即可，时间复杂度O(M+N),M是A的长度，N是B的长度。

其他扫描线的题目
[56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)
[57. 插入区间](https://leetcode-cn.com/problems/insert-interval/)
[732. 我的日程安排表 III](https://leetcode-cn.com/problems/my-calendar-iii/)

[LeetCode Link](https://leetcode-cn.com/problems/interval-list-intersections/)
[GitHub Link](https://github.com/larui529/LeetCode/tree/master/SweepLine/986.%20%E5%8C%BA%E9%97%B4%E5%88%97%E8%A1%A8%E7%9A%84%E4%BA%A4%E9%9B%86)