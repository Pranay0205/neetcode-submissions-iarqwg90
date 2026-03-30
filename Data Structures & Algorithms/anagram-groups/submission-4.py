class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupAnagrams = {}

        for word in strs:
            wordHash = [0] * 26
            for letter in word: 
                wordHash[ord(letter) - ord('a')] += 1
            hashKey = tuple(wordHash)
            if hashKey in groupAnagrams:
                groupAnagrams[hashKey].append(word)
            else:
                groupAnagrams[hashKey] = [word]

        return list(groupAnagrams.values())