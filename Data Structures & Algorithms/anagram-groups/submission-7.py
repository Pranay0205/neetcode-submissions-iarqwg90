class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 1. create a freqMap so for cat it will be tuple(1, 0, 1, 0,...1,...0): ["cat", "act"]
        # 2. For index c - 96 ord(a) = 2, a = 0

        freqMap = {}
        
        for word in strs:
            freq = [0] * 26
            for l in word:
                freq[ord(l) - ord("a")] += 1
            
            if tuple(freq) in freqMap:
                freqMap[tuple(freq)].append(word)
            else:
                freqMap[tuple(freq)] = [word] 
    
        
        return list(freqMap.values())


        