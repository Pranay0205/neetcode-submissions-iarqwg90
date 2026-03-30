class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        originalSet = set()
        for num in nums:
            if num in originalSet:
                return True
            originalSet.add(num)
        
        return False