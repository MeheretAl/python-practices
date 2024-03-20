from collections import defaultdict


def badPairCount(nums: list[int]) -> int:
    goodCounter = 0
    dict1 = defaultdict(int)

    size = len(nums)
    totalPairs = int((size * (size - 1)) / 2)
    return totalPairs - goodCounter


nums = [1, 2, 3, 4, 5, 6]
print(badPairCount(nums))
