class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        nums.sort()
        i = 0
        j = i + 1
        count = 0
        max_streak = 0
        print(nums) # [2, 3, 4, 4, 5, 10, 20]
        while(j < len(nums) and i < j):
            
            if nums[i] == nums[j]:
                i += 1
                j += 1
                continue

            diff = abs(nums[j] - nums[i])
            print(diff)
            if diff == 1:
                count += 1
                max_streak = max(count, max_streak)
            else:
                count = 0
            
            
            i += 1
            j += 1

        return max_streak + 1
        