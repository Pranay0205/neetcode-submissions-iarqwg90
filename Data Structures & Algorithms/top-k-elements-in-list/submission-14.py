class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}
        

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
     
       
        sortedMap =  sorted(freqMap, key= lambda x: freqMap[x], reverse=True)
        result = []
        for i, n in enumerate(sortedMap):
            if i == k:
                break
            
            result.append(n)
            
        return result