class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq = {}

        is_anagram = False
        
        for letter in s:
            if letter not in letter_freq:
                letter_freq[letter] = 1
            else:
                letter_freq[letter] += 1
        

        for letter in t:
            if letter not in letter_freq:
                is_anagram = False
                return is_anagram
            else:
                letter_freq[letter] -= 1

        for letter in s:
            if letter_freq[letter] != 0:
                return is_anagram
        
        is_anagram = True

        return is_anagram
    


