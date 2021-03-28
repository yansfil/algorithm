"""
https://leetcode.com/problems/course-schedule-ii/
위상 정렬 문제로 indegree graph를 따로 둬서 차수가 0인 애들을 지속적으로 queue로 넣는다.
"""

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {}
        graph = collections.defaultdict(list)
        for num in range(numCourses):
            indegree[num] = 0
        for a, b in prerequisites:
            graph[b] += [a]
            indegree[a] += 1

        queue = []
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)
        result = []
        while queue:
            k = queue.pop(0)
            result.append(k)
            for v in graph[k]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return result if len(result) == numCourses else []