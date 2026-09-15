class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}
        

        for n in nums:
            if n in freqMap:
                freqMap[n] = 1 + freqMap.get(n, 0)
            else:
                freqMap[n] = 0
       
        sortedMap =  sorted(freqMap, key= lambda x: freqMap[x], reverse=True)
        result = []
        for i, n in enumerate(sortedMap):
            if i == k:
                break
            
            result.append(n)
            
        return result