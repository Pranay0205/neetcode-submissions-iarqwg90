class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [] * 2 * n 
        print(n * 2)
        for i in range(n * 2):
            ans.append(nums[i % n])

        return ans
