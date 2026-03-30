class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # initialize the freq array with arrays
        freq = [[] for i in range(len(nums) + 1)] 

        # get the count of each element and store it in dictionary
        for n in nums:
            count[n] = 1 + count.get(n, 0) 

        # append the count to freq array with number as index
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # reverse iterate the freq array and take out the top K frequent elements
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        