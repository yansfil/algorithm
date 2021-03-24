"""
https://leetcode.com/problems/longest-increasing-subsequence/
단순한 포인터 방식으로 O(N^2)
이분탐색 사용하면 O(NlogN) -> 참신
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        max_list = [1] * len(nums)
        max_list[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    max_list[i] = max(max_list[i], max_list[j] + 1)
        return max(max_list)


import bisect
def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                index = bisect.bisect_left(dp, nums[i])
                dp[index] = nums[i]
                print(dp)
        return len(dp)

print(lengthOfLIS([10,9,2,5,3,1,101,18]))

