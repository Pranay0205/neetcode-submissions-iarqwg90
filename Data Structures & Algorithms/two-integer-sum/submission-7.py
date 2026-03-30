class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashNums = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashNums and hashNums[complement] != i:
                return [hashNums[complement], i]
            else:
                hashNums[num] = i
        
        return []
      