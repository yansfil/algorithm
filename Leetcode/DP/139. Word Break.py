"""
https://leetcode.com/problems/word-break/

전형적인 DP 문제다
포함된 sub word가 있으면 DP에서 True로 표시하고 점진적으로 값을 확인한다.

"""

class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        ### BOTTOM UP ###
        # dp = [False] * (len(s)+1)
        # dp[0] = True
        # for i in range(1,len(s)+1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordDict :
        #             dp[i] = True
        #             break
        # return dp[-1]

        ### TOP DOWN ###
        dp = {}
        dp[""] = True

        def backtrack(s):
            if s in dp:
                return dp[s]
            ans = False
            for idx in range(len(s)):
                if s[:idx + 1] in wordDict:
                    ans = ans | backtrack(s[idx + 1:])
            dp[s] = ans
            return ans

        return backtrack(s)