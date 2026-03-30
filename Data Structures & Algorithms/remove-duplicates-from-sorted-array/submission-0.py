class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = set()

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] not in unique_nums:
                nums[slow] = nums[fast]
                unique_nums.add(nums[fast])
                slow += 1
               
            fast += 1
        
        return slow