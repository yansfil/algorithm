"""
순열 함수를 재귀로 구현해봄
참고로 list(str포함)에서 index range를 쓸 때 범위를 초과해도 에러가 나지 않는다. 그냥 빈 배열만 나옴
"""


def permutation(arr, n):
    ret = []
    if n == 1:
        for v in arr:
            ret.append([v])
        return ret
    for i in range(len(arr)):
        for v in permutation(arr[:i]+arr[i+1:],n-1):
            ret.append([arr[i]]+v)
    return ret

def combination(arr,n):
    ret = []
    if n == 1 :
        for v in arr:
            ret.append([v])
        return ret
    for i in range(len(arr)):
        for v in combination(arr[i+1:], n-1):
            ret.append([arr[i]]+v)
    return ret


print(permutation([1,2,3], 3))
print(combination([1,2,3], 3))