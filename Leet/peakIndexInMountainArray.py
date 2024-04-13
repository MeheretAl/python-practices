def peakIndexInMountainArray(arr:list[int]) -> int:
    if len(arr) == 3:
        return 1
    left,right = 0, len(arr) - 1
    while left < right:
        mid = (left+right) // 2
        leftSide = arr[mid-1]
        rightSide = arr[mid+1]
        if  arr[mid-1]  > arr[mid]:
            right = mid
        elif arr[mid+1] > arr[mid]:
            left = mid
        else:
            return mid

    return mid
