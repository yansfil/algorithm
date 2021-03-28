"""
https://leetcode.com/problems/accounts-merge/
email끼리 그래프를 만들어야 함. 이때 모든 그래프의 관계를 그리기보단,
name <- first email <-> all emails
이런 구조로 가져가면 그래프 탐색을 통해서 문제를 해결할 수 있을 듯
"""


import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        e_name_table = {}
        email_table = collections.defaultdict(set)
        for row in accounts:
            name = row[0]
            emails = row[1:]
            for email in emails:
                e_name_table[email] = name
                email_table[email].add(emails[0])
                email_table[emails[0]].add(email)

        def dfs(email, seen, res):
            if email in seen: return
            res.append(email)
            seen.add(email)
            for nei in email_table[email]:
                dfs(nei, seen, res)

        seen, result = set(), []
        for email in e_name_table:
            res = []
            if email not in seen:
                dfs(email, seen, res)
                result.append([e_name_table[email]] + sorted(res))
        return result

