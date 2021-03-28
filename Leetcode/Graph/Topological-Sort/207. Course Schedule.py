"""
https://leetcode.com/problems/course-schedule/
전형적인 위상정렬 문제이다. 보통 Queue를 이용해서 많이 구현한다고 함.
BFS 알고리즘을 사용해서 차레대로 소거해나가보자

너무 DFS에만 얽메이지 말고, BFS, DFS 자유롭게 사용하기
recursive가 헷갈리면 stack이나 queue로 풀어도 된다.
"""

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for i in range(numCourses):
            degree[i] = 0
        for p in prerequisites:
            graph[p[1]] += [p[0]]
            degree[p[0]] += 1
        queue = []
        for k, v in degree.items():
            if v == 0:
                queue.append(k)
        result = []
        while queue:
            v = queue.pop(0)
            result.append(v)
            for item in graph[v]:
                degree[item] -= 1
                if degree[item] == 0:
                    queue.append(item)

        return len(result) == numCourses
