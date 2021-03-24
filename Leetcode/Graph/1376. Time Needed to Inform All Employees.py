"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
매니저와 서브 매니저의 관계가 Tree임을 이해하고 이를 adjacent matrix로 표현해야 한다.
그리고 이를 recursive하게 가져가기
"""

import collections
class Solution:
    max_time = 0
    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        man2sub = collections.defaultdict(list)
        for sub, man in enumerate(manager):
            man2sub[man].append(sub)
        def dfs(head, cur, maxtime):
            if not man2sub[head]: #리프노드라는 것을 알 수 있음.
                return max(maxtime, cur)
            for sub in man2sub[head]:
                maxtime = dfs(sub, cur+informTime[head], maxtime)
            return maxtime
        return dfs(headID, 0, 0)
