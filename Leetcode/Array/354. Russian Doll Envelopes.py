"""
https://leetcode.com/problems/russian-doll-envelopes/

Longest Increasing Subsequence랑 비슷한 문제다.
다만 Width를 오름차순, Height를 내림차순으로 정렬하는 것만 다름
"""

from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: [[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -1 * x[1]))
        arr = []
        for envelop in envelopes:
            idx = bisect_left(arr, envelop[1])
            if len(arr) == idx:
                arr.append(envelop[1])
            else:
                arr[idx] = envelop[1]
        return len(arr)
