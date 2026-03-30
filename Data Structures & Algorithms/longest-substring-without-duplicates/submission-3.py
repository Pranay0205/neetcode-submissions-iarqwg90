class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        LetterSet = set()
        maxLength = 0
        l , r = 0 , 0

        for r in range(len(s)):
            while s[r] in LetterSet:
                LetterSet.remove(s[l])
                l += 1
            LetterSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)       
        
        return maxLength
            
            

        