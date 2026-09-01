class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]

        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, heights[l])
                res += maxL - heights[l]
            else:
                r -= 1
                maxR = max(maxR, heights[r])
                res += maxR - heights[r]
        return res

            
            


        