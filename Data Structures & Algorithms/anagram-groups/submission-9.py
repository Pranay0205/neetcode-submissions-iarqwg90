class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

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


        