"""
https://leetcode.com/problems/satisfiability-of-equality-equations/
Union Find 기본적인 문제임
"""


class Solution:
    def equationsPossible(self, equations: [str]) -> bool:
        # Union Find 풀이
        parent = {}
        def find(x):
            if x not in parent:
                return x
            return find(parent[x])

        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 != p2:
                parent[p2] = p1

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[-1])

        for eq in equations:
            if eq[1] == "!" and find(eq[0]) == find(eq[-1]):
                return False
        return True

        # DFS 풀이
        graph = collections.defaultdict(set)
        not_equals = []
        for eq in equations:
            if eq[1] == "=":
                graph[eq[0]].add(eq[-1])
                graph[eq[-1]].add(eq[0])
            else:
                not_equals.append([eq[0], eq[-1]])

        def dfs(node, target, visit):
            if node == target:
                return True
            visit.append(node)
            for x in graph[node]:
                if x in visit:
                    continue
                if dfs(x, target, visit):
                    return True
            return False

        for a, b in not_equals:
            if dfs(a, b, []):
                return False
        return True





