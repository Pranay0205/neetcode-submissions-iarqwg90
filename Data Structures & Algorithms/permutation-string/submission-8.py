class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sb1 = "".join(sorted(s1))
        l = 0
        # Iterate only until the window can fit
        while l <= len(s2) - len(s1): 
            sb2 = "".join(sorted(s2[l : l + len(s1)]))
            # print(sb1, sb2)
            if sb2 == sb1:  # Changed s1 to sb1
                return True
            l += 1
        
        return False