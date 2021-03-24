"""
https://leetcode.com/problems/possible-bipartition
dislike인 애들을 color(0,1)의 반대로 넣어서 끝까지 잘 가면 True 못가면 False
BFS ,DFS 모두 적용 가능하며 coloring을 위한 dictionary를 따로 생성한다.
이를 Two Coloring Graph라고 한다.
https://velog.io/@cheol/Meetcode-2020-07-04-Leetcode.-886.-Possible-Bipartition

"""


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = {}

        for v in range(1, N + 1):

            if v not in colors:
                queue = [(v, 0)]
                while queue:
                    v, color = queue.pop(0)
                    if v in colors:
                        if colors[v] != color:
                            return False
                        continue
                    colors[v] = color
                    for d in graph[v]:
                        queue.append((d, color ^ 1))
        return True

