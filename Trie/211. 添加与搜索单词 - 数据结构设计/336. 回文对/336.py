class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        res = set()
        lookup = {}

        def add(word, tree, index):
            for e in word:
                if e not in tree:
                    tree[e] = {}
                tree = tree[e]
            tree['#'] = index

        for i in range(len(words)): 
            add(words[i], lookup, i)

        def search(word, tree):
            if not word:
                if '#' in tree:
                    return tree['#']
                return -1
            for e in word:
                if e not in tree:
                    return -1
                tree = tree[e]
            if '#' not in tree:
                return -1
            return tree['#']


        def is_panlindrome(word):
            l, r = 0, len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        
        # print (lookup)

        for i in range(n):
            l = len(words[i])
            # print (l)
            for j in range(l+1):
                # print (words[i], words[i][:j])
                if is_panlindrome(words[i][:j]):
                    # print (words[i][j:])
                    index = search(words[i][j:][::-1], lookup)
                    # print ('first', index, i)
                    # print (words[i][j:][::-1], index)
                    if index != -1 and index!= i:
                        res.add((index, i))
                if is_panlindrome(words[i][j:]):
                    index = search(words[i][:j][::-1], lookup)
                    # print (index, i)
                    if index != -1 and index !=i:
                        res.add((i, index))
        return list(res)