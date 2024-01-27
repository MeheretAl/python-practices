def cyclicSort(arr: list[int]) -> list[int]:
    answer = []
    i = 0
    while(i < len(arr)):
        index = arr[i] - 1
        if (arr[i] != arr[index]):
            arr[i] , arr[index] = arr[index] , arr[i]
        else:
            i+=1

    for i in range(1,len(arr)):
        if i != arr[i-1]:
            answer.append(i)
            
    return answer

nums = [4,3,2,7,8,2,3,1]
answer = cyclicSort(nums)
print(answer)