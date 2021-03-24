"""
https://leetcode.com/problems/longest-palindromic-substring/
홀수, 짝수의 기준에 맞춰 중앙에서 옆으로 뻗어나가는 방식으로 구현했음
DP 문제로도 풀 수 있다고 함
참고 https://leetcode.com/problems/longest-palindromic-substring/discuss/119765/Python-DP-solution
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 :
            return s
        max_cnt = 0
        result = None
        for i in range(1,len(s)):
            left, right = i-1, i+1
            cnt_odd = 1
            #홀수
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cnt_odd += 2
                    left -= 1
                    right += 1
                    continue
                break
            if max_cnt < cnt_odd:
                max_cnt = cnt_odd
                result = s[left+1:right]
            #짝수
            left, right= i-1, i
            cnt_even = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cnt_even += 2
                    left -= 1
                    right += 1
                    continue
                break
            if max_cnt < cnt_even:
                max_cnt = cnt_even
                result = s[left+1:right]
        return result