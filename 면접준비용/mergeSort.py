def merge(a,b):
    left = right = 0
    result = []
    while left < len(a) and right < len(b):
        if a[left] > b[right]:
            result.append(b[right])
            right += 1
        else :
            result.append(a[left])
            left += 1
        result += b[right:]
        result += a[left:]
    return result

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left,right)

print(merge_sort([5,4,3,2,1,10,4,6]))



