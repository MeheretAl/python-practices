from collections import defaultdict


def badPairCount(nums: list[int]) -> int:
    goodCounter = 0
    dict1 = defaultdict(int)
    for i, n in enumerate(nums):
        goodCounter += dict1[n - i]
        dict1[n - i] += 1
    size = len(nums)
    totalPairs = int((size * (size - 1)) / 2)
    return totalPairs - goodCounter


nums = [1, 2, 3, 4, 5, 6]
print(badPairCount(nums))
