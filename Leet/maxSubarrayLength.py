from collections import defaultdict


def maxSubLength(k: int, nums: list[int]) -> int:
    freq = defaultdict(int)
    left, answer = 0, 0
    for i in range(len(nums)):
        freq[nums[i]] += 1
        if freq[nums[i]] > k:
            while nums[left] != nums[i]:
                freq[nums[left]] -= 1
                left += 1
            freq[nums[left]] -= 1
            left += 1
        answer = max(answer, i - left + 1)
    return answer
