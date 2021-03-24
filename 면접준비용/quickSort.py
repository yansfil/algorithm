def simple_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left_arr = []
    right_arr = []
    mid_arr = []
    for v in arr:
        if v > pivot:
            right_arr.append(v)
        elif v < pivot:
            left_arr.append(v)
        else :
            mid_arr.append(v)
    return simple_quick_sort(left_arr) + mid_arr + simple_quick_sort(right_arr)

# print(simple_quick_sort([1,2,3,4,5,6,7,8]))

# In-place 방식

def quick_sort(arr):
    def sort(left, right):
        if left >= right:
            return
        mid = partition(left,right)
        sort(left,mid-1)
        sort(mid, right)

    def partition(left,right):
        mid = (left+right)//2
        pivot = arr[mid]
        while left <= right:
            while pivot > arr[left]:
                left += 1
            while pivot < arr[right]:
                right -= 1
            if left <= right :
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left
    sort(0, len(arr)-1)
    return arr


[10,8,5,1,2]

print(quick_sort([1,2,3,4,5,6]))