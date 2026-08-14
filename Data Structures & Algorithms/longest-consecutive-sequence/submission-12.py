class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # convert the array to a set as duplicates has no use 
        numset = set(nums)

        # find the all starters of sequence first
        starters = []
        for num in numset:
            if num - 1 not in numset:
                starters.append(num)
        
        # go over each starters and count the longest sequence
        maxcount = 0
        for num in starters:
            count = 0
            while num in numset:
                count += 1
                num += 1
            maxcount = max(maxcount, count)
        
        return maxcount