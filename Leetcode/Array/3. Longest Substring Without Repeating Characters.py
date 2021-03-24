"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
투 포인터 기법을 활용해서 left, right로 점점 전진시키면서 최대 길이를 구한다.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        max_length = 0
        arr = []
        while r < len(s):
            if s[r] not in arr:
                arr += s[r]
                r += 1
            else :
                while s[l] != s[r]:
                    l += 1
                l += 1
                arr = s[l:r]
            max_length = max(r-l, max_length)
        return max_length