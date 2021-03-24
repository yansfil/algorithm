"""
https://leetcode.com/problems/target-sum/
그냥 백트래킹으로는 시간 제한이 걸려 안풀린다. DP 사용해야함
DP 조건 잘 캐치하는 게 중요함
꼭 Recursive하게만 생각하지 말 것. 값을 쌓아올리는 방식 Bottom Up, Top Down 모두 생각할 수 있다
"""

# DFS
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}

        def dfs(i, target):
            if i == len(nums):
                cnt = 0
                if target == S:
                    cnt = 1
                return cnt
            if (i, target) in memo:
                return memo[(i, target)]

            a = dfs(i + 1, target - nums[i])
            b = dfs(i + 1, target + nums[i])
            memo[(i, target)] = a + b
            return a + b

        dfs(0, 0)
        return memo[(0, 0)]
# BFS

class Solution:
   # BFS:summary,cnt in queue
   def findTargetSumWays(self, nums: List[int], S: int) -> int:
        import collections
        queue = {0:1}
        for n in nums:
            tmp = collections.defaultdict(int)
            print(queue)
            for summary,cnt in queue.items():
                tmp[summary+n]+=cnt
                tmp[summary-n]+=cnt
            print(tmp)
            queue = tmp
           # print(queue)
        return queue[S]