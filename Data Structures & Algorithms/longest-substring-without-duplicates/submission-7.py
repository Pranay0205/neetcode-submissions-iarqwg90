class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_set = set()
        l, r = 0, 0
        max_length = 0
        while r < len(s):
            while s[r] in letter_set:
                letter_set.remove(s[l])
                l += 1
            
            letter_set.add(s[r])

            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length