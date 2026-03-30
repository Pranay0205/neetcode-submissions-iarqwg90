class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumDif = {}

        for i, n in enumerate(nums):
           
            difference = target - n

            if difference in sumDif:
                return [sumDif[difference], i]

            sumDif[n] = i
        return
            
                

          

