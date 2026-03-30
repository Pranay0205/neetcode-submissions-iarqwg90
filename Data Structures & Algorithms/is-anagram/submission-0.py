class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sdict = {}

        for letter in s:
            if letter not in sdict:
                sdict[letter] = 1
            else:
                sdict[letter] += 1

        tdict = {}
       
        for letter in t:
            if letter not in tdict:
                tdict[letter] = 1
            else:
                tdict[letter] += 1

        return sdict == tdict
            

        

        