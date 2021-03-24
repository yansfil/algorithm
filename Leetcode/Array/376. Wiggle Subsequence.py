"""
https://leetcode.com/problems/wiggle-subsequence/
DP 혹은 Greedy로 풀 수 있는 문제
"""

class Solution:
    def wiggleMaxLength(self, nums: int) -> int:
        if len(nums) == 1:
            return 1
        up = [1] * len(nums)
        down = [1] * len(nums)
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0 :
                up[i] = max(down[i-1]+1, up[i-1])
            elif diff < 0 :
                down[i] = max(up[i-1]+1, down[i-1])
            else :
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(up[-1],down[-1])
