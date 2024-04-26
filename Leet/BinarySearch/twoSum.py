def twoSum(nums: list[int], target: int) -> list[int]:
    size = len(nums)
    left = 0
    right = size - 1
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]
    return[left+1,right+1]