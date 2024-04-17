def cyclesort(arr:list[int]):
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i] - 1
        if arr[i] > 0 and arr[i] != arr[correctIndex] :
            arr[i] , arr[correctIndex] = arr[correctIndex] , arr[i]
        else:
            i+=1

    print(arr)

nums = [0,1,0,3,12]
cyclesort(nums)
