class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupAnagrams = {}

        result = []

        for word in strs:
            sorted_string = ''.join(sorted(word))

            if sorted_string not in groupAnagrams:
                groupAnagrams[sorted_string] = [word]
            else:
                groupAnagrams[sorted_string].append(word)
        
        for key in groupAnagrams:
            result.append(groupAnagrams.get(key))

 

        return result




        