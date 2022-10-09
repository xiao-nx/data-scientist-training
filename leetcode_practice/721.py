from typing import List, Dict
from collections import defaultdict

# https://leetcode.com/problems/subarray-product-less-than-k/

# 定义并查集
class UF:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]

    def find(self, a: int) -> int:
        if a == self.parent[a]:
            return a
        return self.find(self.parent[a])

    def union(self, a: int, b: int):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            self.parent[bp] = ap
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 为所有 account 创建一个并查集。具有相同 email 的 account 连接到一个集合中
        uf = UF(len(accounts))

        # 每个 email 地址到它所在的 account 在 accounts 中的 index
        emailOwner: dict[str, int] = {}

        # 遍历每个 account
        for i, ac in enumerate(accounts):
            # 遍历一个 account 的每个 email
            for email in ac[1:]:
                # 如果这个 email 之前遍历过，则在 emailOwner 中保存了它的 owner account 的 index
                # owner 有可能还是这个 account，即 emailOwner[email] = i
                # 也有可能是另一个 account，那么就需要在并查集中合并这两个 account
                if email in emailOwner:
                    index = emailOwner[email]
                    # 不管 email 的 owner 是否和 account i 是同一个，直接合并就可以
                    uf.union(i, index)
                # 在 emailOwner 中保存这个 email 的 owner 是索引为 i 的 account，为之后的 email 遍历来查找
                emailOwner[email] = i
        # 已经在并查集中合并了同一个人的所有 account，但是并查集中是以树的方式组织的，现在将这些 account 合并为 list
        ret: Dict[int, List[str]] = defaultdict(list)
        # 遍历每个 email
        for email, owner in emailOwner.items():
            # 查找 email 在并查集中的 root account index
            root = uf.find(owner)
            # 将这个 email 追加到 root 的 list 中
            ret[root].append(email)
        # 将每个 account 的 email list 排序，并加上 account 的 name，得到最终结果
        return [accounts[i][:1] + sorted(arr) for i, arr in ret.items()]
            

test = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]
]

s = Solution()
ret = s.accountsMerge(test)
print(ret)
