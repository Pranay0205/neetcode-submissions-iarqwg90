class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring = set()

        l, r = 0, 0
        max_substring = 0
        while r < len(s):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            r += 1
            max_substring = max(max_substring, r - l)
        
        return max_substring 
            
