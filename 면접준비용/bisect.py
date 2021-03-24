def binary_search(arr, target, left):
    i = 0
    j = len(arr)
    while i < j:
        mid = (i+j) // 2
        if arr[mid] > target:
            j = mid
        elif arr[mid] < target:
            i = mid+1
        else :
            if left:
                j = mid
            else:
                i = mid + 1
    return i

print(binary_search([1,2,3,4,6],6,False))