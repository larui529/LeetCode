class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

       
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        n = len(people)
        res = []

        for i in range(n):
            res.insert(people[i][1], people[i])
        return res
            