from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Brute force n^2
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    m = {}
    for i in range(len(nums)):
        m[nums[i]] = i
    
    for i in range(len(nums)):
        if target-nums[i] in m.keys() and i != m[target-nums[i]]:
            return [i, m[target-nums[i]]]