"""
https://leetcode.com/problems/task-scheduler/

수학적으로 계산하는 방법이 있고
n(제한)기준으로 시간을 1씩 Count하는 방법이 있음
"""

from heapq import heappop, heappush
from collections import Counter
class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)

        return curr_time