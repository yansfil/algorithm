"""
https://leetcode.com/problems/merge-sorted-array/
two pointer를 활용해서 잘 merge하기
"""

class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:

        while n:
            if m and nums1[m] > nums1[n]:
                nums1[n+m-1] = nums1[m]
                m-=1
            else :
                nums1[n+m-1] = nums2[n]
                n-=1