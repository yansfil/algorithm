"""
https://leetcode.com/problems/redundant-connection/
DFS방식으로 하면 전체 순회를 한 후 차곡차곡 소거하면서 다 순회가 되는 지 확인해야 한다 -> BAD
Union Find 방식으로 하나씩 순회하면서 cycle이 되는 지를 확인하면 바로 풀 수있음 -> GOOOD
"""



# DFS 방식 (BAD)
import collections
class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a] += [b]
            graph[b] += [a]

        def traverse(a, visit=set()):
            visit.add(a)
            for v in graph[a]:
                if v not in visit:
                    traverse(v, visit)

        for a, b in edges[::-1]:
            graph[a].remove(b)
            graph[b].remove(a)
            visit = set()
            traverse(a, visit)
            if len(visit) == len(edges):
                return [a, b]
            graph[a] += [b]
            graph[b] += [a]

# Union Find 방식(Good)

class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        parent = {}

        def find(x):
            if x not in parent:
                return x
            return find(parent[x])

        #Union 과정에서 싸이클이 생기는 지도 확인할 수 있다
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 == p2:
                return 0
            else:
                parent[p2] = p1
                return 1

        for a, b in edges:
            if not union(a, b):
                return [a, b]


