class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        combos = []
        for s, e in A:
            combos.append([s, 1])
            combos.append([e,-1])
        for s,e in B:
            combos.append([s,1])
            combos.append([e,-1])
        combos = sorted(combos, key=lambda x: (x[0], -x[1]))
        count = 0
        start, end = 0, 0
        res = []
        for t, f in combos:
            count+=f
            if count==2:
                start = t
            elif count==1 and f ==-1:
                end = t
                res.append([start, end])
        return res