"""
https://leetcode.com/problems/open-the-lock/
최단 경로를 구하는 문제는 BFS로 문제를 푼다.
"""

import collections
class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        queue = collections.deque([("0000", 0)])
        visit = set("0000")
        deadends = set(deadends)
        while queue:
            now, cnt = queue.popleft()
            if target == now:
                return cnt
            if now in deadends:
                continue
            for idx in range(4):
                digit = int(now[idx])
                for way in [1, -1]:
                    move = (digit + way) % 10
                    goal = now[:idx] + str(move) + now[idx + 1:]
                    if goal not in visit:
                        visit.add(goal)
                        queue.append((goal, cnt + 1))

        return -1

