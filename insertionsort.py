def insertionSort(arr: list[int]) -> list[int]:
    for i in range(1,len(arr)):
        j = i
        while(arr[j-1] > arr[j] and j > 0):
            #swap
            arr[j] , arr[j-1] = arr[j-1] , arr[j]
            j-=1
    
    return arr

