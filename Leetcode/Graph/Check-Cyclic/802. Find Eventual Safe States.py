"""
https://leetcode.com/problems/find-eventual-safe-states/
cyclic하지 않은 것을 감별하기 위해선,
1. DFS 방식으로 visited에 값을 넣으면서 visited에 값이 존재하면 cyclie로 간주하기
2. indegree, outdegree를 활용해서 outdegree의 차수가 0인 애들은 Terminal Node이므로 queue에 넣으면서 확인하기 (Topological Sort와 유사하다)
3. colouring 기법을 사용해서 visit을 True ,False가 아닌 0(not start),1(process),2(complete) 로 바꿔서 순회시킨다. 이를 통해 cyclic 하지 않은 애들은 2,한 애들은 1로 뽑을 수 있
"""

# 1번 : DFS (느리다) -> visited같은 경우 set을 하는게 조회 속도를 O(1)로 높일 수 있다.
class Solution:
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        result = set()
        def dfs(i, visited):
            for j in graph[i]:
                if j in visited:
                    return False
                if j in result:
                    continue
                visited.add(j)
                if not dfs(j, visited):
                    return False
                visited.remove(j)
            result.add(i)
            return True
        for idx in range(len(graph)):
            visited = set()
            dfs(idx, visited)
        return sorted(list(set))

# 2번 : indegree, outdegree 활용하기
import collections
class Solution:
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        indegree, outdegree = collections.defaultdict(set), collections.defaultdict(int)

        queue = []
        result =[]
        for idx in range(len(graph)):
            outdegree[idx] = len(graph[idx])
            if len(graph[idx]) == 0:
                queue.append(idx)
            for j in graph[idx]:
                indegree[j].add(idx)

        while queue:
            v = queue.pop(0)
            result.append(v)
            for k in indegree[v]:
                outdegree[k] -= 1
                if outdegree[k] == 0:
                    queue.append(k)

        return sorted(result)

# 3번 : colouring
import collections
class Solution:
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        visit = [0] * len(graph)
        def dfs(i):
            visit[i] = 1
            for j in graph[i]:
                if visit[j] == 0:
                    dfs(j)
                if visit[j] == 1:
                    return
            visit[i] = 2
        for i in range(len(graph)):
            if visit[i] == 0: dfs(i)
        return [ i for i in range(len(graph)) if visit[i] == 2]