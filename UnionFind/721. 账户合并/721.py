from typing import List
from collections import defaultdict

class UF:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    n = len(accounts)
    uf = UF(n)
    email_to_id = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_id:
                uf.union(i, email_to_id[email])
            else:
                email_to_id[email] = i
    groups = defaultdict(set)
    for email, idx in email_to_id.items():
        root = uf.find(idx)
        groups[root].add(email)
    res = []
    for root, emails in groups.items():
        name = accounts[root][0]
        res.append([name] + sorted(emails))
    return res

if __name__ == '__main__':
    ac = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnny@mail.com"]]
    print(accountsMerge(ac))
