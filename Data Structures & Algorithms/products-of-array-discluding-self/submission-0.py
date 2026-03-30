class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix = [1] * size
        suffix = [1] * size
        result = [1] * size

        i = 1
        while(i < size):           
            prefix[i] = nums[i - 1] *  prefix[i - 1]
            i += 1
        
        i = size - 2
        while(i >= 0):
            suffix[i] =  nums[i + 1] * suffix[i + 1]
            i -= 1

        for i in range(size):
            result[i] = prefix[i] * suffix[i]


        return result




