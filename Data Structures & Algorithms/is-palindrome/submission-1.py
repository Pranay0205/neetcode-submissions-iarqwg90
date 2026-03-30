class Solution:
    def isPalindrome(self, s: str) -> bool:

        rs = ""
        new_s  = ""
        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()
            
        for i in range(len(new_s) - 1, -1, -1):
            if new_s[i].isalnum():
                rs += new_s[i].lower()
            else:
                continue

        return new_s == rs
        