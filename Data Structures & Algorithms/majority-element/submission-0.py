class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        Mnums = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            Mnums[num] += 1
            if maxCount < Mnums[num]:
                res = num
                maxCount = Mnums[num]
        
        return res
        
