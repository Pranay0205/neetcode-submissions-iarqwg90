class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointer method 
        # one pointer at the end and one at the start
        l, r = 0, len(s) - 1

        # iterate over each letter and check if it is alphanumeric if it is skip it or increment it
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            
            while r > l and not s[r].isalnum():
                r -= 1
            
        # other wise compare it
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True