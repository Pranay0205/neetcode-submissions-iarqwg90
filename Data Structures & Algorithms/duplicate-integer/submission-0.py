class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_numset = set()

        for num in nums:
            if num not in unique_numset:
                unique_numset.add(num)
            else:
                return True
        
        return False

         