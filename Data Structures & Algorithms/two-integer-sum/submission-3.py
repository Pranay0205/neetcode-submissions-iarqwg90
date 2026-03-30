class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        twoDict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in twoDict:
                return [twoDict[complement], i]
            twoDict[num] = i
        