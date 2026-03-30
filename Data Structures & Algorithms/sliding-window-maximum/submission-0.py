class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        for i in range(len(nums) - k + 1):
            current_max = nums[i]
            for j in range(i, i + k):
                current_max = max(nums[j], current_max)
            res.append(current_max)
        
        return res
