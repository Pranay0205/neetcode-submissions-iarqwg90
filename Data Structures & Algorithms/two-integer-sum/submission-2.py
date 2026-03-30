class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevmap and prevmap[diff] != i:
                return [prevmap[diff], i]
            
            prevmap[num] = i
        
        


        