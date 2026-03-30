class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashNums = {}

        for i, num in enumerate(nums):
            if num in hashNums:
                return True
            else:
                hashNums[num] = i
        
        return False
        