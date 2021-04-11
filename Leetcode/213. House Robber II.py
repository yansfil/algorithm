"""
https://leetcode.com/problems/house-robber-ii/

MAX값을 구하기 위해선 DP 방식으로 접근할 수 있다.
그러나 예외조건은 circular임. circular 한 방향의 최댓값을 구하는 문제이다.
이를 단순화 하면 단순하게 맨 처음을 제외한 Array, 맨 마지막을 제외한 Array 두개에 대해 Max 값을 구한 후 최대값을 구하면 된다.

"""


class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def getMax(nums):
            dp = [0] * len(nums)
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[0] + nums[2]
            for i in range(3, len(nums)):
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            return max(dp)

        return max(getMax(nums[1:]), getMax(nums[:-1]))