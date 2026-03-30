class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            if nums[i] == 1:
                count_1 += 1
            if nums[i] == 2:
                count_2 += 1
                
        i = 0
        while count_0:
            nums[i] = 0
            count_0 -= 1
            i += 1
        
        while count_1:
            nums[i] = 1
            count_1 -= 1
            i += 1
        
        while count_2:
            nums[i] = 2
            count_2 -= 1
            i += 1
            
                