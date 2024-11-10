from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numberIndex = {}
        
        for i, x in enumerate(nums):
            complement = target - x
            
            if complement in numberIndex:
                return [numberIndex[complement], i]
            
            numberIndex[x] = i