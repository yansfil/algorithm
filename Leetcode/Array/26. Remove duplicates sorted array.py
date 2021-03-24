"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
O(n)으로 처리할 수 있도록 포인터 위치를 잘 옮겨보자
"""


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1