class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for letter in s:
            stack.append(letter)
        i = 0
        while stack:
            s[i] = (stack.pop())
            i += 1
