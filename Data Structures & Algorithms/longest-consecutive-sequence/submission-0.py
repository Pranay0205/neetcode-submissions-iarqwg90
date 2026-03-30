class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        longestSequence = 0

        isSequenceStart = False

        for i in range(len(nums)):
           
            if nums[i] - 1 not in numset:
                isSequenceStart = True
            
            if isSequenceStart:
                currentNum = nums[i]
                res = 0
                while currentNum in numset:
                    res += 1
                    currentNum += 1

            isSequenceStart = False   
            longestSequence = max(longestSequence, res)
            
        return longestSequence