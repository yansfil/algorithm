"""
https://leetcode.com/problems/rotate-array
in-place 로 sorting하기 위해선 결국 reverse와 관련된 트릭을 알아야 한다.
"""

class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        end = len(nums)-1
        self.reverse(nums,0,end-k)
        self.reverse(nums,end-k+1,end)
        self.reverse(nums,0,end)
