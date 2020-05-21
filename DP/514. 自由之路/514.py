class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        import copy
        from collections import defaultdict
        capital2rings = defaultdict(list)
        n = len(ring)
        newRing = ""
        for i in range(n):
            newRing =ring[i:]+ring[:i]
            capital2rings[ring[i]].append([newRing, i])
        
        # print (capital2rings)
        key = '#'+key
        l = len(key)
        dp = [[float('inf')]*n for i in range(l)]
        possibleCurrentStates = [0]
        dp[0][0] = 0

        for i in range(1, l):
            for currState in possibleCurrentStates:
                newPossibleSatets = []
                for newRing, newState in capital2rings[key[i]]:
                    if newState==currState:
                        dp[i][newState] = min(dp[i][newState], 1+dp[i-1][currState])
                    else:
                        moves = abs(newState-currState)
                        dp[i][newState] = min(dp[i][newState], dp[i-1][currState]+1+moves, dp[i-1][currState]+1+(n-moves))
                    newPossibleSatets.append(newState) 
                possibleCurrentStates = copy.deepcopy(newPossibleSatets)
        # print (dp)
        return min(dp[-1])
                