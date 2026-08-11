class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numIndMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in numIndMap:
                return [numIndMap[complement], i]
            numIndMap[n] = i
        
         



        