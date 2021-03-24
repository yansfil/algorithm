"""
https://leetcode.com/problems/longest-absolute-file-path/
참고 : https://leetcode.com/problems/longest-absolute-file-path/discuss/86780/Clear-python-Solution
list에서 복수의 인덱스 값을 바꿀 수 있다.
arr = [1,2,3,4]
arr[1:] = [7,8]
arr # 1,7,8

순서가 보장되어있는 상황에서 list의 값을 인덱스 별로 통째로 업데이트시키고 싶을 때 사용
"""
import collections

## Dictionary 사용해서 풀기
class Solution1:
    def lengthLongestPath(self, input: str) -> int:
        max_depth = 0
        table = collections.defaultdict(str)
        for line in input.split("\n"):
            cnt = line.count('\t')
            table[cnt] = line.strip('\t')
            if "." in table[cnt]:
                length = 0
                for i in range(cnt + 1):
                    length += len(table[i])
                max_depth = max(max_depth, length + cnt)
        return max_depth

## List 사용해서 풀기
class Solution2:
    def lengthLongestPath(self, input:str) -> int:
        path = []
        max_depth = 0
        for line in input.split("\n"):
            cnt = line.count("\t")
            path[cnt:] = [line.strip("\t")]
            if "." in path[-1]:
                max_depth = max(max_depth, "/".join(path))
        return max_depth