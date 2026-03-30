class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kfrequent = {}
        result = []

        for num in nums:
            if num not in kfrequent:
                kfrequent[num] = 1
            else:
                kfrequent[num] += 1

        sorted_dict = dict(sorted(kfrequent.items(), key=lambda item: item[1], reverse = True))

        index = 0
        for key in sorted_dict:
            if index >= k:  
                break;   
            result.append(key)
            index += 1     
        

        return result
                
        