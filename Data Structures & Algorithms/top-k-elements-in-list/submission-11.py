class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1
            
        result = sorted(freqMap.keys(), key = lambda x: freqMap[x], reverse=True)

        return result[:k]