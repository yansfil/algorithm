"""
https://leetcode.com/problems/insert-interval
stack에 차곡차곡 interval를 쌓아올린다. 만약 마지막 스택값이 현재 보는 스택값과 관련이 있다면 스택을 터뜨리고 새로운 스택을 처리한다
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        stack = [intervals[0]]
        while intervals:
            now = intervals.pop(0)
            prev = stack[-1]
            if prev[1] >= now[0]:
                stack.pop()
                stack.append([prev[0], prev[1] if prev[1] > now[1] else now[1]])
            else:
                stack.append(now)
        return stack


