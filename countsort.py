def countSort(arr : list[int]):
    maxValue = max(arr);
    freq = [0] * (maxValue + 1)
    for i in range(len(arr)):
        freq[arr[i]] += 1

    index = 0
    for i in range(maxValue+1):
        while(freq[i] > 0):
            arr[index] = i
            index+=1;
            freq[i]-=1

    print(arr)
    
    
    

arr = [1,0,3,1,3,1]
countSort(arr=arr)

