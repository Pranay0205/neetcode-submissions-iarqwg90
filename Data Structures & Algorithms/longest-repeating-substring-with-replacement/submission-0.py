class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            # Increment the count of the letter
            count[s[r]] = 1 + count.get(s[r], 0)

            # Shrink the window till it is valid
            while(r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # Check the max substring which contains only one distinct character.
            res = max(res, r - l + 1)
        
        return res