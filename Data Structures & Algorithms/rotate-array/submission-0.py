class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [0] * len(nums)

        size = len(nums)

        for i in range(size):
            result[(i + k) % size] = nums[i]

        for i in range(size):
            nums[i] = result[i] 



