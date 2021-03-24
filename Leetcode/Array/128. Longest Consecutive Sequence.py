"""
https://leetcode.com/problems/longest-consecutive-sequence/
set -> list로 중복 제거 후 정렬한 후 순차적으로 순회하면서 연속된 값일 때 count를 늘린다.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        max_count = 1 
        cnt = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == prev+1 :
                cnt += 1 
                if i == len(nums)-1:
                    max_count = max(cnt, max_count)
            else:
                max_count = max(cnt, max_count)
                cnt = 1
            prev = nums[i]
        return max_count

# O(N)으로 처리하기 (Set -> 포인터 기법 사용하기)
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
            max_cnt = 0
            while nums:
                v = nums.pop()
                up = v + 1
                down = v - 1
                cnt = 1
                while up in nums:
                    cnt += 1
                    nums.remove(up)
                    up += 1
                while down in nums:
                    cnt += 1
                    nums.remove(down)
                    down -= 1
                max_cnt = max(max_cnt, cnt)
            return max_cnt
