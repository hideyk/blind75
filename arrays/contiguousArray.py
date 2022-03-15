from audioop import findmax
from typing import List, Tuple

def findMaxLength(nums: List[int]) -> int:
    res = 0
    
    for i in range(len(nums)):
        zeros, ones = 0, 0
        for n in nums[i:i+res]:
            zeros += (1 - n)
            ones += n

        for l in range(res+2, len(nums)+1, 2):
            if i + l > len(nums):
                break

            for n in nums[i+l-2:i+l]:
                zeros += (1 - n)
                ones += n

            if ones == zeros:
                res = max(l, res)
            
        if i + res + 2 > len(nums):
            break
    return res

arr = [0,1,1,0,1,1,1,0]
a = findMaxLength(arr)
print(a)