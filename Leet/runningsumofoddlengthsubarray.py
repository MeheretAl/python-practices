
def sumOddLengthSubarrays(arr: list[int]) -> int:
    length = len(arr)
    result = []

    for i in range(length):
        subarray = []
        for k in range(i, length, 2):
            subarray = arr[i:k + 1]
            result.append(sum(subarray))

    answer = sum(result)
    return answer


print(sumOddLengthSubarrays([1,4,2,5,3]))