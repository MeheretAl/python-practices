from collections import defaultdict


def countSubArrays(nums: list[int], k: int) -> int:
    length = len(nums)
    if length < k:
        return 0
    maxElement = max(nums)
    left, right, answer = 0, 0, 0
    freq = defaultdict(int)
    while right < length:
        freq[nums[right]] += 1
        while freq[maxElement] >= k:
            answer += length - right
            freq[nums[left]] -= 1
            left += 1
        right += 1

    return answer

