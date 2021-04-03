"""
https://leetcode.com/problems/increasing-triplet-subsequence/
Consequtive Sequence의 연장선으로 풀 수 있음
1. first, second 변수 활용하기 -> logical하게 어떻게 짜냐가 중요한 듯
2. bisect 활용하기
"""

import bisect


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 변수 활용하기
        #         if len(nums) < 3 :
        #             return False

        #         first = second = float('inf')

        #         for num in nums:
        #             if num <= first :
        #                 first = num
        #             elif first < num < second:
        #                 second = num
        #             elif second < num:
        #                 return True
        #         return False

        # bisect 이용하기
        arr = []
        for num in nums:
            idx = bisect.bisect_left(arr, num)
            if idx == len(arr):
                arr.append(num)
            else:
                arr[idx] = num
            if len(arr) == 3:
                return True
        return False
