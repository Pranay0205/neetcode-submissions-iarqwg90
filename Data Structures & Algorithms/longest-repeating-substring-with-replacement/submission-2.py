class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}

        l, r = 0, 0
        max_count = 0
        res = 0
        for r in range(len(s)):
            count_map[s[r]] = 1 + count_map.get(s[r], 0)
            max_count = max(max_count, count_map[s[r]])

            while (r - l + 1) - max_count > k:
                count_map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
